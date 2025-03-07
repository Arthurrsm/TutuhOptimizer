import os
import subprocess
import psutil
import customtkinter as ctk
from tkinter import messagebox
import winreg

# Configuração da interface gráfica
ctk.set_appearance_mode("System")  # Modo de aparência (System, Dark, Light)
ctk.set_default_color_theme("blue")  # Tema de cores

class OptimizationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Otimizador do Windows - Gamer Edition")
        self.geometry("1000x800")

        # Criar abas
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        # Abas
        self.tabview.add("Limpeza")
        self.tabview.add("Desempenho")
        self.tabview.add("Inicialização")
        self.tabview.add("Sistema")
        self.tabview.add("Jogos")

        # Widgets da aba "Limpeza"
        self.clean_temp_button = ctk.CTkButton(self.tabview.tab("Limpeza"), text="Limpar Arquivos Temporários", command=self.clean_temp_files)
        self.clean_temp_button.pack(pady=10)

        self.clean_cache_button = ctk.CTkButton(self.tabview.tab("Limpeza"), text="Limpar Cache DNS", command=self.clean_dns_cache)
        self.clean_cache_button.pack(pady=10)

        # Widgets da aba "Desempenho"
        self.high_performance_button = ctk.CTkButton(self.tabview.tab("Desempenho"), text="Ativar Modo Alto Desempenho", command=self.set_high_performance)
        self.high_performance_button.pack(pady=10)

        self.defrag_button = ctk.CTkButton(self.tabview.tab("Desempenho"), text="Desfragmentar Disco (C:)", command=self.defrag_disk)
        self.defrag_button.pack(pady=10)

        # Widgets da aba "Inicialização"
        self.startup_label = ctk.CTkLabel(self.tabview.tab("Inicialização"), text="Programas de Inicialização:")
        self.startup_label.pack(pady=10)

        self.startup_listbox = ctk.CTkTextbox(self.tabview.tab("Inicialização"), height=200)
        self.startup_listbox.pack(pady=10, fill="x")

        self.refresh_startup_button = ctk.CTkButton(self.tabview.tab("Inicialização"), text="Atualizar Lista", command=self.refresh_startup_list)
        self.refresh_startup_button.pack(pady=10)

        self.disable_startup_button = ctk.CTkButton(self.tabview.tab("Inicialização"), text="Desativar Programa Selecionado", command=self.disable_startup_program)
        self.disable_startup_button.pack(pady=10)

        # Widgets da aba "Sistema"
        self.system_info_label = ctk.CTkLabel(self.tabview.tab("Sistema"), text="Informações do Sistema:")
        self.system_info_label.pack(pady=10)

        self.system_info_text = ctk.CTkTextbox(self.tabview.tab("Sistema"), height=200)
        self.system_info_text.pack(pady=10, fill="x")

        self.refresh_system_info_button = ctk.CTkButton(self.tabview.tab("Sistema"), text="Atualizar Informações", command=self.refresh_system_info)
        self.refresh_system_info_button.pack(pady=10)

        # Widgets da aba "Jogos"
        self.reduce_input_lag_button = ctk.CTkButton(self.tabview.tab("Jogos"), text="Reduzir Input Lag", command=self.reduce_input_lag)
        self.reduce_input_lag_button.pack(pady=10)

        self.disable_updates_button = ctk.CTkButton(self.tabview.tab("Jogos"), text="Desativar Atualizações Automáticas", command=self.disable_windows_updates)
        self.disable_updates_button.pack(pady=10)

        self.uninstall_bloatware_button = ctk.CTkButton(self.tabview.tab("Jogos"), text="Desinstalar Bloatware", command=self.uninstall_bloatware)
        self.uninstall_bloatware_button.pack(pady=10)

        # Inicializar dados
        self.refresh_startup_list()
        self.refresh_system_info()

    # Funções de otimização
    def clean_temp_files(self):
        try:
            temp_dirs = [os.environ.get("TEMP"), os.environ.get("TMP"), os.path.join(os.environ.get("SystemRoot"), "Prefetch")]
            for temp_dir in temp_dirs:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        os.remove(os.path.join(root, file))
                    for dir in dirs:
                        os.rmdir(os.path.join(root, dir))
            messagebox.showinfo("Sucesso", "Arquivos temporários limpos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao limpar arquivos temporários: {e}")

    def clean_dns_cache(self):
        try:
            subprocess.run(["ipconfig", "/flushdns"], check=True)
            messagebox.showinfo("Sucesso", "Cache DNS limpo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao limpar cache DNS: {e}")

    def set_high_performance(self):
        try:
            subprocess.run(["powercfg", "/s", "SCHEME_MIN"], check=True)
            messagebox.showinfo("Sucesso", "Modo de alto desempenho ativado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ativar modo de alto desempenho: {e}")

    def defrag_disk(self):
        try:
            subprocess.run(["defrag", "C:", "/U", "/V"], check=True)
            messagebox.showinfo("Sucesso", "Desfragmentação do disco concluída!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao desfragmentar disco: {e}")

    def refresh_startup_list(self):
        try:
            startup_items = []
            for proc in psutil.process_iter(['pid', 'name']):
                startup_items.append(f"{proc.info['name']} (PID: {proc.info['pid']})")
            self.startup_listbox.delete("1.0", "end")
            self.startup_listbox.insert("1.0", "\n".join(startup_items))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar lista de inicialização: {e}")

    def disable_startup_program(self):
        try:
            selected_program = self.startup_listbox.get("1.0", "end").strip()
            if selected_program:
                subprocess.run(["taskkill", "/f", "/im", selected_program.split()[0]], check=True)
                messagebox.showinfo("Sucesso", f"Programa {selected_program} desativado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao desativar programa: {e}")

    def refresh_system_info(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage("/")
            system_info = (
                f"Uso da CPU: {cpu_usage}%\n"
                f"Uso de Memória: {memory_info.percent}%\n"
                f"Uso de Disco: {disk_usage.percent}%\n"
                f"Total de Memória: {memory_info.total / (1024 ** 3):.2f} GB\n"
                f"Total de Disco: {disk_usage.total / (1024 ** 3):.2f} GB"
            )
            self.system_info_text.delete("1.0", "end")
            self.system_info_text.insert("1.0", system_info)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar informações do sistema: {e}")

    def reduce_input_lag(self):
        try:
            # Desativar efeitos visuais
            subprocess.run(["powercfg", "/setactive", "SCHEME_MIN"], check=True)
            subprocess.run(["systempropertiesperformance"], shell=True)

            # Ajustar prioridade de processos
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "Win32PrioritySeparation", 0, winreg.REG_DWORD, 26)
            winreg.CloseKey(key)

            messagebox.showinfo("Sucesso", "Input Lag reduzido com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reduzir input lag: {e}")

    def disable_windows_updates(self):
        try:
            subprocess.run(["sc", "config", "wuauserv", "start=", "disabled"], check=True)
            subprocess.run(["sc", "stop", "wuauserv"], check=True)
            messagebox.showinfo("Sucesso", "Atualizações automáticas desativadas!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao desativar atualizações: {e}")

    def uninstall_bloatware(self):
        try:
            bloatware = [
                "Microsoft.YourPhone",
                "Microsoft.SkypeApp",
                "Microsoft.ZuneMusic",
                "Microsoft.ZuneVideo",
                "Microsoft.WindowsMaps",
                "Microsoft.BingWeather",
                "Microsoft.BingNews",
                "Microsoft.XboxApp",
                "Microsoft.XboxGameOverlay",
                "Microsoft.XboxIdentityProvider",
                "Microsoft.XboxSpeechToTextOverlay",
            ]
            for app in bloatware:
                subprocess.run(["Get-AppxPackage", app, "|", "Remove-AppxPackage"], shell=True)
            messagebox.showinfo("Sucesso", "Bloatware desinstalado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao desinstalar bloatware: {e}")

# Executar o aplicativo
if __name__ == "__main__":
    app = OptimizationApp()
    app.mainloop()