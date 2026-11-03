---
article_id: 20148239979799
category: Originação de Grãos (OG)
content_hash: 1ced12ccdd3d7ad0059a4b506c7bacff647ce9e9b3d037b0a48f5c7c6138c566
fetched_at: '2026-06-28T22:45:36.959159+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Alteração do campo NJJ_QTDFIS no Romaneio
type: support-article
updated_at: '2025-01-09T20:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20148239979799-Agro-Linha-Protheus-AGR-Altera%C3%A7%C3%A3o-do-campo-NJJ-QTDFIS-no-Romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20148208520727) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para alterar o campo **NJJ\_QTDFIS** é apresentada a ocorrência **Alteração do campo NJJ\_QTDFIS no Romaneio**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é preciso realizar o o processo para alterar o campo **NJJ\_QTDFIS** no Romaneio.  
  
**Solução**  
Para solucionar essa ocorrência, realize a regra para editar o campo ou não, é a seguinte:

![Roma.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20148239960471)

Somente permitimos editar o campo **NJJ\_QTDFIS - Quantidade Fiscal** quando:  
**Formulário Próprio = 2 Não**, ou seja, são **Romaneios de Entrada,** **Compra**, **Remessa para Depósito**, **Devolução**, **Retorno de Depósito** onde não é necessário gerar nota fiscal, pois o **fornecedor** cliente nestas situações já encaminharam uma **nota fiscal DANFE**, e assim estas informações devem ser informadas conforme o documento recebido.  
**Tipo de Controle = 2 Sem Pesagem**, ou seja são **Romaneio simbólicos, sem pesagem OGA251**, onde as informações são informadas manualmente, em geral para dar entrada de **nota fiscal DANFE de complementos de quantidade por diferença de pesagem**, onde não há peso físico, apenas fiscal, ou outras situações de exceções sem pesagem, que foram necessárias.  
  
Esta consistência, além do campo de quantidade fiscal, também está nos campos:  
**NJJ - Romaneio - NJJ\_DOCSER - Serie NF**  
**NJJ - Romaneio - NJJ\_DOCNUM - Numero NF**  
**NJJ - Romaneio - NJJ\_DOCEMI - Emissao NF**  
**NJJ - Romaneio - NJJ\_DOCESP - Especie NF**  
**NJJ - Romaneio - NJJ\_QTDFIS - Qtd. Fiscal**  
**NJJ - Romaneio - NJJ\_VLRUNI - Vlr. Unit.**  
**NJJ - Romaneio - NJJ\_VLRTOT - Vlr. Total**  
  
Qual impacto de retirar ou mesmo customizar esta consistência:  
Quando o cliente decide customizar, deve efetuar teste completo nas rotinas relacionadas e observar os impactos. Não temos como prever impactos, pois vai depender do que for customizado e qual a resultado que se espera com isso.  
Sobre retirar esta consistência, o impacto é que o campo ficará livre para ser informado manualmente em qualquer condição.  
Efetuando testes completos, após este ajuste podem ser seja identificado outros pontos de customizações, para que informações erradas não sejam permitidas, ou ainda inibir outras atualizações ou validações do produto sobre esse campo.  
Todos os testes de produto, automatizados ou manuais, são realizados da forma original que foi liberado, sendo assim os futuros desenvolvimentos e impactos estarão cobertos por eles desde que o mesmo não tenha sofrido alterações.
