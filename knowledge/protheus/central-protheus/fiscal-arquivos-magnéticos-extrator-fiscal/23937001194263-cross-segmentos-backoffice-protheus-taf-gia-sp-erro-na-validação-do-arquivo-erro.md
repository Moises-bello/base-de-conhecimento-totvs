---
article_id: 23937001194263
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 91ef983a0e6f52965eeeb2f3679631a7b5c3d6f881f0c905d4cc5e1554ae9082
fetched_at: '2026-06-28T22:42:07.967634+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - GIA-SP - Erro na Validação do
  Arquivo - Erro: Tabela 03, CR=10, Campo – Imposto Inconsistente, Posição 39, linha
  nº  4'
type: support-article
updated_at: '2024-06-04T17:20:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23937001194263-Cross-Segmentos-Backoffice-Protheus-TAF-GIA-SP-Erro-na-Valida%C3%A7%C3%A3o-do-Arquivo-Erro-Tabela-03-CR-10-Campo-Imposto-Inconsistente-Posi%C3%A7%C3%A3o-39-linha-n%C2%BA-4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23937001174679) Tempo aproximado para leitura: **00:02:00 min**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF – Nova GIA –  Todas as versões.  
  
**Ocorrência**

Ao validar o arquivo **GIA SP** é apresentada a seguinte mensagem: "**Sr(a) usuário (a) entre em contato com a empresa responsável pela geração do arquivo Pré-Formatado e informe a mensagem abaixo:****Tabela 03, CR=10, Campo - Imposto**  
**Inconsistente, Posição 39**  
**Linha nº 4****Causa**  
Geralmente essa inconsistência ocorre, quando a **Nota Fiscal** possui o imposto **ICMS**, porém, não possui as informações de **Alíquota**, **Base de Cálculo** e/ou **Valor do Imposto**, ou o **CFOP** da operação não é condizente com os valores lançados na **Base de Cálculo/Alíquota/Valor**, e a regra de **ICMS** vinculada ao **CFOP**.

**Solução**  
Para solucionar essa ocorrência, siga os passos abaixo, verifique a escrituração da **Nota Fiscal**.  
  
01. Abra o **arquivo txt**, e identifique qual **CFOP**é criticada na **linha 4**;

*Print:*

![imagem gia.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23945386544791)  
02. Gere a **Apuração do ICMS**;  
03. Verifique se está faltando alguma informação referente ao **imposto ICMS**, nos lançamentos com o **CFOP** demonstrado no **arquivo GIA**.

04. Localize as **Notas Fiscal** com o **CFOP** demonstrado, e avalie se há alguma inconsistência na **Base de Cálculo, Alíquota, Valor,** ou na **Natureza de Operação**.

05. Ajuste o lançamento incorreto ou a regra de **ICMS** do **CFOP**.

06. Após seguir os passos acima, realize a escrituração novamente,  realize a integração no **TAF**.

07. Acesse a rotina **Central de Obrigações** (**TAFOBRIG**), e gere um novo arquivo **GIA** e valide-o.

Para mais informações acesse:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020316311-MP-FIS-Procedimento-Completo-Nova-GIA>

*Link* **Manual da Nova GIA-SP - Pré-formatado-NG.** https://portal.fazenda.sp.gov.br/servicos/gia/Downloads/pre\_formatado\_ngia\_v0210\_gia0801.pdf
