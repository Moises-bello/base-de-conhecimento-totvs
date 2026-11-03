---
content_hash: 82e6382c72046b1d1e76be55952183833b1cc24bc0d115fe9918093a2a3b3745
fetched_at: '2026-06-29T00:06:27.973841+00:00'
page_id: '233742226'
product: rm
source: tdn-rm
title: EDU0002 - WebSerivice via ( Host )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233742226
version: 3
---

# Assunto: WebService via ( Host )

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional x LMS Fluig |
| **Versões:** | 12.1.10 |
| **Ocorrência:** |  |
| **Ambiente:** | SQL |
| **Passo a passo:** | Configurando WS – TOTVS Educacional ( Host )   Localizar a Pasta RM.Net  Editar estes 3 Arquivos Configs      Editar RM.Host.exe.Config  **Editar a tag** <add key="Port" value="VALOR DA PORTA A UTILIZAR" />  **Adicionar as Tags**:  <add key="DBAlias" value="CORPORERM"/> Alias do Banco de dados  <add key="DEFAULTDB" value="CORPORERM"/> Alias do Banco de Dados  <add key="UseTOTVSESB" value="true" />  **Remover se existir a Tag** : <add key="Host" value="localhost"/>  pois com ela fica LocalHost em todas  localizações e fica com erro no LMS .   * Editar o arquivo RM.exe.config   **Editar as tags** <add key="Port" value="PORTA UTILIZADA NO HOST" /> e               <add key="Host" value="NOME DO SERVIDOR" />    Depois de alterar os 3 arquivos Configs ( Fechar o Host – Serviço ou Local - Deletar o Broker.dat e reinicia-lo em seguida.     Finalizar o Host   Deletar o Broker     Reiniciar o Host.exe   **Testando conexão WS RM ( Host )**  [http://](http://10.31.6.33:8051/EAIService/IConWSEAIService)10.31.6.33:8051/EAIService/IConWSEAIService   ( IP da maquina na qual encontra-se o host )     **Informar o IP da máquina** na qual o Host encontra-se iniciado ou nome da Máquina     Caminho que deve ser enviado para o LMS parametrizar a Integração:       Excluir ( /IConWSEAIService ) – ENTER     Clicar no Link acima            * Enviar o caminho :  <http://10.31.6.96:8051/EAIService/mex?wsdl>   Alterar o nome do PC para IP da máquina na qual o WS encontra-se. * Porta: **RM\_IConWSEAIService** ( como é informado na figura acima ) * Usuário e senha RM  -  (  mestre – totvs  ) |
| **Observações:** |  |
