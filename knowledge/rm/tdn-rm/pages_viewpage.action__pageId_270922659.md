---
content_hash: 2ff5d575f62830e6aded677acae89bac8c2ad5cd46ded452df07235214f0ad2f
fetched_at: '2026-06-29T00:08:25.697992+00:00'
page_id: '270922659'
product: rm
source: tdn-rm
title: BD0017_Oracle_Versão_Client
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270922659
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | Oracle |
| **Ocorrência:** | Verificar versão do client Oracle instalado |
| **Ambiente:** | RM |
| **Passo a passo:** | Para iniciar os testes de conexão quanto ao Oracle: Abra o prompt de comandos do Windows através do botão Iniciar, executar, cmd, ok.    Digite então *SQLPLUS usuario/senha@servidor/instancia* conforme exemplo abaixo:     Outro teste que devemos realizar é através do Net Manager, seguindo os seguintes passos:   1. Iniciar: 2. Criar 3. Nome do serviço 4. Protocolo 5. Nome do serviço no Oracle 6. Nome do servidor 7. Testar 8. Alterar login 9. Testar conexão 10. Finalizar 11. Conferir no arquivo *oracle\product\11.2.0\client\_64\network\admin\tnsnames.ora*  Verificando as versões 32 ou 64 do client instalado na máquina Abra o prompt de comandos do Windows através do botão Iniciar, executar, regedit, ok.    32 - bits: Verificar se existe o diretório *Key\_OraClient* na pasta *Oracle*:    64 - bits: Verificar se existe o diretório *Key\_OraClient* na pasta *Oracle*:     Client Oracle - Instalação do client 32 e 64 bits do Oracle na mesma máquina  <http://tdn.totvs.com/x/j49pCw> |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 –(Banco de Dados) |
