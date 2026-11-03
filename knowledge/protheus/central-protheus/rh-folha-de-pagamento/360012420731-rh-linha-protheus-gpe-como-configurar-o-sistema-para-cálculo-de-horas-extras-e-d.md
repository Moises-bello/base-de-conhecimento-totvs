---
article_id: 360012420731
category: RH - Folha de Pagamento
content_hash: 13668076be80aef18e18e313a13a0c5876f48a16a4c6df439512c1401fefe47b
fetched_at: '2026-06-28T22:44:13.332731+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o Sistema para cálculo de Horas
  Extras e DSR para Comissionado
type: support-article
updated_at: '2025-09-15T19:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012420731-RH-Linha-Protheus-GPE-Como-configurar-o-Sistema-para-c%C3%A1lculo-de-Horas-Extras-e-DSR-para-Comissionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26251730812951) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como configurar o Sistema para cálculo de Horas Extras e DSR sobre comissão para funcionários Comissionados.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No Módulo Gestão de Pessoal (SIGAGPE), crie uma nova verba para pagamento de Hora Extra sobre Comissão.  
  
Acesse **Atualizações > Definições de Cálculo >  Verbas**  e clique em incluir  
Essa verba será **associada** à verba de hora extra original, geralmente aplicada sobre a parte fixa da remuneração do empregado, a qual é denominada de verba de hora extra principal, pois ela fica referenciada dessa forma, mais adiante, nesse procedimento.  
  
1. Preencha os campos das demais pastas de modo idêntico ao cadastro da verba de hora extra principal, mas atenção: o campo **Percentual** deve contemplar **apenas** o adicional da hora extra; Exemplo: se a verba principal for hora extra 50%, informe nesse campo apenas 50,00.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794181468055)

Após edição, clique em **Confirmar**.  
  
2. Ainda no cadastro de Verbas, posicione o cursor sobre **a verba de hora extra principal** e clique em **Alterar.**  
No campo **Cod.Corresp**., informe **a verba de hora extra de comissão**  criada no passo 1 e clique em **Confirmar.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794181473175)**

Realize os procedimentos descritos acima para cada uma das verbas de hora extra que entrará na movimentação do funcionário.  
  
3. Para lançamento das verbas, acesse **Atualizações > Lançamentos > Por Funcionário**. Selecione um funcionário comissionado e clique em Incluir.  
Faça o lançamento da verba de **comissão** com id de cálculo **0165** com valor da comissão, informe também a verba de **hora extra principal** com a quantidade de horas que ele tem direito e clique em salvar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794181473943)  
  
4. Realize o cálculo da folha em **Miscelânea > Cálculos > Por roteiro.**  
  
5. Acesse novamente a rotina de Lançamentos em **Atualizações > Lançamentos Por Funcionário.** Selecione o empregado comissionado, clique em Visualizar, verifique se foram geradas ou valorizadas as verbas abaixo:  
**Horas Extras** - Verba principal lançada

**Horas extras sobre comissão** - Verba criada no item 1 e relacionada a verba de Hora extra principal

**DSR sobre horas extras** - Quando a verba de Hora extra principal estiver configurada para cálculo de DSR

**DSR sobre comissões** - Quando a verba de comissão estiver configurada para cálculo de DSR  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794181479319)  
  
**Observações**  
Se o empregado for um **comissionado puro** (sem salário especificado no cadastro de funcionários) a verba a ser informada deve ser, **obrigatoriamente**a verba de hora extra referente às comissões que foi criada no passo 1. Caso contrário, trata-se de um comissionado misto, e a verba a ser informada deve ser a **verba de hora extra principal**.  
  
**Integração SIGAPON x SIGAGPE na Rescisão de Contrato de Trabalho (GPEM040)**  
Quando for solicitar a **importação** dos **Resultados** do **Ponto Eletrônico** no Cálculo de **Rescisão,** para comissionado **puro** (sem salário no cadastro de Funcionários - GPEA010), os resultados de horas extras do Ponto Eletrônico são direcionados para as verbas de **horas extras** sobre as comissões.  
  
**Saiba Mais**[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

<https://tdn.totvs.com/pages/releaseview.action?pageId=245172200>
