---
article_id: 360057804914
category: RH - FGTS / SEFIP
content_hash: 892f0074df828f7b2c21e94496c4a44afbcf39199a6b36025b105047edd401bf
fetched_at: '2026-06-28T22:43:41.140616+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Ao enviar a SEFIP  ocorre o erro 300548 - Base
  de Cálculo 13º Salário Previdência Social - Referente à competência do movimento
  deve ser informada para trabalhadores com movimentação definitiva (exceto rescisão
  por justa causa)
type: support-article
updated_at: '2026-06-26T18:25:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057804914-RH-Linha-Protheus-GPE-Ao-enviar-a-SEFIP-ocorre-o-erro-300548-Base-de-C%C3%A1lculo-13%C2%BA-Sal%C3%A1rio-Previd%C3%AAncia-Social-Referente-%C3%A0-compet%C3%AAncia-do-movimento-deve-ser-informada-para-trabalhadores-com-movimenta%C3%A7%C3%A3o-definitiva-exceto-rescis%C3%A3o-por-justa-causa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34697635022359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao enviar a SEFIP é apresentado o seguinte erro: 300548 - Base de Cálculo 13º Salário Previdência Social - Referente à competência do movimento deve ser informada para trabalhadores com movimentação definitiva (exceto rescisão por justa causa)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esse erro ocorre  quando o funcionário não recebeu valores de 13º Salário na rescisão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Para resolver a inconsistência, no SEFIP após aparecer a mensagem *Validação do Arquivo finalizada com sucesso*, acesse o menu: M*ovimento > Empresa;*  
2. Em seguida, abra a modalidade e selecione o funcionário. Na guia Movimento do Trabalhador, selecione Dados do Movimento;  
3.No item Base de Cálculo 13º Salário Previdência Social - Referente à Competência do Movimento:

* Informe o valor 0,01.
* Após, clique em Salvar e confirme a alteração.
* Feche a modalidade.
* Marque o código de recolhimento para voltar na opção *Simular*.

![](https://suporte.metadados.com.br/hc/article_attachments/360014845772/mceclip3.png)

**Saiba Mais:**

[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS)

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
