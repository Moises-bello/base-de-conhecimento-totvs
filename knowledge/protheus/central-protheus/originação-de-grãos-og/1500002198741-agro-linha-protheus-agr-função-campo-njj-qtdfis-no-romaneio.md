---
article_id: 1500002198741
category: Originação de Grãos (OG)
content_hash: 76a3c16a4fb1090d128c6f34661ec6da5506679ab2db77ca7e19b0b1c3e8ebd2
fetched_at: '2026-06-28T22:45:39.500133+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Função Campo NJJ_QTDFIS no Romaneio
type: support-article
updated_at: '2025-06-26T11:23:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002198741-Agro-Linha-Protheus-AGR-Fun%C3%A7%C3%A3o-Campo-NJJ-QTDFIS-no-Romaneio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20141505150871)***Tempo aproximado para leitura:**00:01:25 min**  
**Dúvida**Qual a função do campo **NJJ\_QTDFIS** e quando pode ser alterado?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**A regra para editar o campo ou não, é a seguinte:

![Roma.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6762697623319)

Somente permitimos editar o campo **NJJ\_QTDFIS - Quantidade Fiscal** quando:  
**Formulário Próprio = 2 Não**, ou seja, são **Romaneios de Entrada,** **Compra**, **Remessa para Depósito**, **Devolução**, **Retorno de Depósito** onde não é necessário gerar nota fiscal, pois o **fornecedor** cliente nestas situações já encaminharam uma **nota fiscal DANFE**, e assim estas informações devem ser informadas conforme o documento recebido.  
**Tipo de Controle = 2 Sem Pesagem**, ou seja são **Romaneio simbólicos, sem pesagem OGA251**, onde as informações são informadas manualmente, em geral para dar entrada de **nota fiscal DANFE de complementos de quantidade por diferença de pesagem**, onde não há peso físico, apenas fiscal, ou outras situações de exceções sem pesagem, que foram necessárias.  
  
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
