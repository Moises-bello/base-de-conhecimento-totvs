---
content_hash: b974698ef8614282e6743e776cec3c367b9dc75dd1215919ad42b198387cdf44
fetched_at: '2026-06-29T00:08:50.307186+00:00'
page_id: '334334050'
product: rm
source: tdn-rm
title: Dicas para reinstalar o TAF/TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334050
version: 2
---

O objetivo desse documento é propor um conjunto de medidas que devem ser adotadas antes de realizar a reinstalação do TAF - Totvs Automação Fiscal.

**Importante!** Vale ressaltar a importância do processo ser realizado ou acompanhado por um analista de TI, visto a necessidade de conhecimento de estrutura de ambiente, redes, etc.**Lembrando que o processo deve ser realizado em um ambiente de homologação.**

1.Acesse a página de Serviços do Windows para **parar** os serviços do TAF e do TSS antes de desinstalar os produtos:

2. Após parar os Serviços do Windows, é necessário deletar os serviços através do Prompt de Comando:

Utilize os comandos abaixo para deletar os serviços:

* **sc delete Taf-Appserver**

* **sc delete Taf-DbAccess**

* **sc delete Taf-Ws**

* **sc delete TSS-Appserver12**

3.Acesse o Painel de Controle e desinstale os programas:

4.Acesse o diretorio de instalação do servidor e exclua as pastas com as instalações antigas (Pastas: TAF e TOTVSSPED):

5.Antes de realizar a reinstalaçãi vailde se o servidor está atendendo os pré requisitos de instalação do TAF:

* [Qual é a infra-estrutura necessária para instalação do TAF?](http://tdn.totvs.com.br/pages/viewpage.action?pageId=190517377)

**Importante!**Para o correto funcionamento das ferramenstas, é necessário criar uma base vazia para cada produdo. Isso significa que o usuário não pode criar o ambiente apontando como base de dados a base que já é utilizada pelo sistema da Linha RM.

**Observações para criação das Bases de Dados:**

**\*\*\*Oracle:**

Criar 2 Bases de dados vazias   :   1 com o nome TAF

                                                         1 com o nome TSS

Criar no TNSNAMES as strings de conexão para ambas as bases.

 Obs: Em caso de SGBD oracle , o servidor deverá possuir o client 12 c 32 bits

**\*\*\*SQL:**

Criar 2 Bases de dados vazias   :   1 com o nome TAF

                                                         1 com o nome TSS

Criar 2 Conexões  ODBC's  para sistema  :   1 com o nome TAF , apontando para a base de dados TAF com usuário e senha.

                                                                         1 com o nome TSS , apontando para a base de dados TSS com usuário e senha.

Obs: O Firewall do Windows deve estar desabilitado e as Portas utilizadas na instalação devem ser liberadas.

### **Fique ligado em nossa playlist com o passo a passo de instalação disponível em nossa página do Youtube!**

**Acesse:** <https://www.youtube.com/playlist?list=PLXa8l0dq5zRmfNY744BnO4Db_SH917WbI>
