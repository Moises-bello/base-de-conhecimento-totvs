---
article_id: 360040836614
category: BI - Business Intelligence - Crystal-Reports
content_hash: f84528de03b9a12c40b1ee3d624d6a220a67ccd76a749f85cb0dbe7c871a96d8
fetched_at: '2026-06-28T22:40:29.051922+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Crystal na release
  12.1.25
type: support-article
updated_at: '2022-07-27T18:31:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040836614-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Crystal-na-release-12-1-25
---

![](https://jiratdncdncontent.blob.core.windows.net/tdn/icons/time.png) Tempo aproximado para leitura: **2** **minuto****Dúvida**Após migração para release 12.25 não estou conseguindo abrir os relatórios **crystal**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Crystal – A partir da versão 12.1.25  
  
**Solução**Ao migrar para a release 25, é necessário proceder com a nova instalação do Crystal.  
Inicialmente é necessário instalar o integrador dentro da pasta do Smart Client de sua máquina.

<https://suporte.totvs.com/portal/p/10098/download#detail/467496>  
  
Seguindo a instalação, configure de acordo com a documentação os arquivos **CRYSINI** e **CRWINI** também dentro do Smart Client. É necessário também que as dlls **apapi.dll** e **apconn.dll** estejam dentro da pasta também.  
  
Não deixe de configurar a conexão do Crystal em seu **ODBC**:  
![](https://totvssuporte.zendesk.com/attachments/token/SHcJEeebFw5rnYgbfFaoPUnvr/?name=inline-1932400262.png)​  
  
Após toda a instalação, será necessário executar o fonte **CRYSCONFIG** que está disponível no pacote abaixo. O pacote pode ser acessado no endereço:  
12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=769402>;  
  
Devido a novas validações do novo DBACCESS será necessário informar o nome do usuário e senha do Protheus e também do Banco de Dados para correta conexão com o banco de dados.  
  
**Saiba Mais:  
[MP - BI - Documentação Crystal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016447592-MP-BI-Documenta%C3%A7%C3%A3o-Crystal?source=search)**
