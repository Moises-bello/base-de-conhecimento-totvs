---
content_hash: c26b0a1fc2619e9b8e37ec55baff95a70d06ea79758d0814079714a1dab55c78
fetched_at: '2026-06-29T00:11:22.605643+00:00'
page_id: '706124960'
product: rm
source: tdn-rm
title: Relação de Api's - Documento técnico (conteúdo Interno) - Minha Contagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706124960
version: 3
---

Relação das Api's que foram criadas para uso no aplicativo "Minha Contagem de Estoque". Neste documento constam detalhes técnicos sobre parâmetros, retorno de cada uma e qual a funcionalidade.

### **Teste via PostMan**

Para realizar a chamada das Api's via PostMan, basta rodar o serviço host como administrador e na configuração deste serviço deve ser informado qual a porta e qual o banco de dados padrão que será utilizado.

Exemplo:

<add key="DEFAULTDB" value="BDTESTE"/>

<add key="APIPORT" value="8051"/>

### Autorização básica

Usuário: mestre

Senha : totvs

observação: Qualquer usuário ativo no RM.
