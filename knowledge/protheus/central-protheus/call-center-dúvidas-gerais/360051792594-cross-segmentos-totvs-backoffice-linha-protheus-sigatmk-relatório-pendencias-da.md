---
article_id: 360051792594
category: Call Center - Dúvidas Gerais
content_hash: 81cc7c8848c402743ec9915a1b39110ab34da2b47c860d456741802601d96466
fetched_at: '2026-06-28T22:41:26.847932+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Relatório Pendencias
  da Agenda
type: support-article
updated_at: '2022-06-17T14:57:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051792594-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Relat%C3%B3rio-Pendencias-da-Agenda
---

**Dúvida**

Como gerar o relatório Relatório Pendencias da Agenda?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - Todas as Versões.

**Solução**

O relatório permite emitir uma relação das cobranças pendentes que estão na carteira do operador, ou seja, só serão impressos os  atendimentos de Telecobrança pendentes.

São impressos: o código/nome do operador, o código/loja do cliente, o telefone/razão social do cliente, CPF/CNPJ do cliente, o total da dívida, a data de envio (data de cobrança), a data/hora de retorno da ligação pendente, o nome completo do cliente, o número do atendimento, a data do atendimento, a operação (ativa ou receptiva), o total por filial, o total por operador, o total geral, etc;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082512574/mceclip0.png)

Para gerar o relatório seguir os procedimentos : 

**INCLUIR ATENDIMENTO TELECOBRANÇA :**   
1- Cadastro de Operador : Perfil Cobrança  
2- Cadastro de Cliente > Outras Ações Contato  
3- Incluir Titulo Vencido > Contas à Receber  
4- Telecobrança > Seleção de Titulo > Gerar = **TMKA180**  
5- Incluir Atendimento > **TMKA271** > Mesmo Cliente / Contato do Titulo vencido                                     6.  Buscar o título "F3" no  campo Titulo > "**ACG\_TITULO**" para trazer o titulo;                                             
7. Alterar o Status= "Cartório" Gravar o Atendimento;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082516214/mceclip1.png)  
8. Gerar o relatório.

*OBS : Os relatórios do Call Center estão diretamente relacionados com o programa TMKRFUN. Este contém funções genéricas de uso interno dos relatórios, portanto, é necessário solicitar este arquivo toda vez que gerado um patch do relatório.*

Detalhes Telecobrança em : **<https://tdn.totvs.com/pages/releaseview.action?pageId=239037537>**
