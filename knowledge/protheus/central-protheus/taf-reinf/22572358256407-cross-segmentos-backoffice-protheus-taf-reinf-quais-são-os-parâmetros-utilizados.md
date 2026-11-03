---
article_id: 22572358256407
category: TAF - REINF
content_hash: 8dd5aab32de4fb81ac991e0df97241299f8a31bd32a66b4a3b5b4b2041ccf5c1
fetched_at: '2026-06-28T22:41:34.777650+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Quais são os parâmetros
  utilizados no Painel Reinf?
type: support-article
updated_at: '2024-04-05T20:50:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22572358256407-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Quais-s%C3%A3o-os-par%C3%A2metros-utilizados-no-Painel-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22572308273047) Tempo aproximado para leitura: **00:06:30min.** **Dúvida**Quais são os parâmetros disponíveis atualmente no **Painel Reinf** dentro do **TAF**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

Os parâmetros abaixo influenciam no comportamento da apuração dos eventos no Painel Reinf se tratando do Bloco 40 de eventos. (R-4010 e/ou R-4020). Segue abaixo:

**MV\_TAFAC20**: Atualmente a rotina de apuração do evento R-4020, considera para apuração os pagamentos (**V3U**), **Faturas avulsas e oriundas de Notas Fiscais (LEM)**, e Notas Fiscais que não tenha uma Fatura relacionada (**C20**). Foi criado parâmetro para não considerar as Notas Fiscais (**C20**) para a apuração do Evento R-4020.

Criação do parâmetro:

| X6\_VAR | X6\_TIPO | X6\_DESCRIC | X6\_CONTEUD |
| --- | --- | --- | --- |
| MV\_TAFAC20 | Lógico | Não apurar as notas fiscais do evento R-4020 | .F. (Default) |

**MV\_TAFCAPR**: Conforme Manual do **Reinf** **versão 2.1.1**, os pagamentos pagos ou creditados a um determinado beneficiário devem ser informados em um único **Arquivo xml**, detalhando-se cada um dos pagamento ou créditos efetuados. Há, no entanto, duas exceções a essa regra:

* Prestação das informações de forma descentralizada por estabelecimento; e
* Utilização do campo {**ideEvtAdic**} no Complemento Cadastral.

Desta forma, foi criado o parâmetro para que seja realizado a Apuração de forma centralizada nas **Filiais** que possuem a mesma **raiz do CNPJ da matriz.**Criação do parâmetro:

| X6\_VAR | X6\_TIPO | X6\_DESCRIC | X6\_CONTEUD |
| --- | --- | --- | --- |
| MV\_TAFCAPR | Lógico | Centraliza apuração eventos R-4010/R-4020? | .F. (Default) |

**MV\_TAFDT40**: Ajustado a apuração dos Eventos R-4010/R-4020 para que seja possível apurar o IR pela data de contabilização do documento.

Este tratamento aplica-se apenas para o IR na emissão (Tributo 12 nos movimentos de Notas Fiscais e Faturas), os títulos com IR no pagamento (tributo 28) devem permanecer considerando apenas a data de pagamento do título.

As seguintes alterações foram realizadas:

* Ajustado os contadores dos Cards dos eventos R4010/R-4020 no painel Reinf;
* Ajustado a tela de pendentes de apuração para trazer somente os movimentos que estiverem dentro da data de emissão ou contabilização conforme parametrização;
* Ajustado a apuração dos Eventos R4010/R-4020, para considerar a opção definida no parâmetro **MV\_TAFDT40**;

Criação do parâmetro:

| X6\_VAR | X6\_TIPO | X6\_DESCRIC | X6\_CONTEUD |
| --- | --- | --- | --- |
| MV\_TAFDT40 | Caracter | Considera a data de contabilização para eventos do bloco 40? 1=Sim;2=Não(Default) | 2 |

**MV\_TAFSTRI**: Foram Realizados ajustes na apuração dos Eventos **R-4010/R-4020,** para considerar movimentações (Nota Fiscal, Fatura ou Pagamento), que contém a Natureza de Rendimento informada mas não houve retenção do IR.

Para que sejam geradas as Apurações desses movimentos sem retenções e enviados para a REINF, foi criado o parâmetro, onde .T., considera movimentos com natureza de rendimento mas que não calcularam impostos (sem tributos) e .F. (Default) não considera movimentos sem tributos, exceto os movimentos que utilizam Naturezas de Rendimentos que não possuem retenções (V3O\_TRIB = 8).

Exemplo: **Nota fiscal de fornecedor do Simples Nacional** sem cálculo de impostos e com Natureza de Rendimento que incide IR/PIS/COFINS/CSLL, somente irá ser apurado para ser enviado ao REINF quando o parâmetro estiver configurado como .T. .

Contudo, os pagamentos com **Natureza de Rendimento que não prevê incidência de nenhum tributo (como, por exemplo, 12001)**, ou movimentos que não atingiram o mínimo de retenção, ou que seja do Grupo 20 da tabela 01, **estes mantém o envio para o Reinf independente da configuração do parâmetro**.

Criação do parâmetro:

| X6\_VAR | X6\_TIPO | X6\_DESCRIC | X6\_CONTEUD |
| --- | --- | --- | --- |
| MV\_TAFSTRI | Lógico | Apura documentos com Nat. Rend. sem tributos | .F. (Default) |

**Para mais detalhes sobre cada parâmetro e a suas funcionalidades, acessar: <https://tdn.totvs.com/display/public/TAF/EFD-Reinf>**
