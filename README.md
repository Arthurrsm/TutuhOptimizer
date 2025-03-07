# TutuhOptimizer

Um programa de otimização do Windows focado em melhorar o desempenho para jogos e uso geral. Desenvolvido em Python com interface gráfica moderna usando `customtkinter`.

---

## Funcionalidades

### Limpeza
- **Limpar Arquivos Temporários:** Remove arquivos das pastas `Temp`, `%Temp%`, e `Prefetch`.
- **Limpar Cache DNS:** Limpa o cache DNS do sistema.

### Desempenho
- **Ativar Modo Alto Desempenho:** Define o plano de energia para alto desempenho.
- **Desfragmentar Disco:** Desfragmenta o disco principal (C:).

### Inicialização
- **Listar Programas de Inicialização:** Exibe programas que iniciam com o Windows.
- **Desativar Programas de Inicialização:** Permite desativar programas selecionados.

### Sistema
- **Informações do Sistema:** Exibe métricas de CPU, memória RAM e uso de disco.

### Jogos
- **Reduzir Input Lag:** Ajusta configurações do sistema para reduzir latência.
- **Desativar Atualizações Automáticas:** Desativa as atualizações automáticas do Windows.
- **Desinstalar Bloatware:** Remove aplicativos pré-instalados desnecessários.

---

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Arthurrsm/tutuh-optimizer.git

2. Instale as dependências:
   ```bash
   pip install customtkinter psutil

3. Execute o programa:
   ```bash
   python tutuh_optimizer.py
   
---

## Versionamento

O programa segue o padrão de versionamento **SemVer** (Semantic Versioning):
- **MAJOR:** Mudanças incompatíveis.
- **MINOR:** Novas funcionalidades compatíveis.
- **PATCH:** Correções de bugs.

### Versões
- **v1.0.0:** Versão inicial com funcionalidades básicas.
- **v1.1.0:** Adicionadas otimizações para jogos (input lag, bloatware, etc.).
- **v1.2.0:** Adicionada otimização de GPU.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](https://github.com/Arthurrsm/TutuhOptimizer/blob/main/LICENSE) para mais detalhes.
