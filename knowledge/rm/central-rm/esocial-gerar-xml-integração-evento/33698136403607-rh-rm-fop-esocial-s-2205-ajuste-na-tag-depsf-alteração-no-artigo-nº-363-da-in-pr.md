---
article_id: 33698136403607
category: eSocial - Gerar XML/ Integração Evento
content_hash: bd7139cc1b3c4f65ad10046c289491ed633ff20c7e8fc3ce902a03927c84ea7f
fetched_at: '2026-06-28T22:47:13.142123+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2205 Ajuste na Tag <depSF> Alteração no Artigo
  nº 363 da IN Pres/INSS nº 28/2022
type: support-article
updated_at: '2026-01-26T15:48:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33698136403607-RH-RM-FOP-eSocial-S-2205-Ajuste-na-Tag-depSF-Altera%C3%A7%C3%A3o-no-Artigo-n%C2%BA-363-da-IN-Pres-INSS-n%C2%BA-28-2022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33698136382359) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Adequar a geração do evento **S-2205 – Alteração de Dados Cadastrais do Trabalhador** para que a tag <depSF> seja preenchida conforme a alteração estabelecida no Art. 363 da **IN Pres/INSS nº 28/2022**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos patches: 12.1.2402.234, 12.1.2406.163, 12.1.2410.101 e superiores  
  
**Solução**  
Foi implementado ajuste para que, na geração do evento S-2205, a tag <depSF> seja gerada com o valor "S" quando o dependente válido possuir idade entre 4 e 14 anos e o campo "Entregou comprov. frequência escolar" estiver marcado no cadastro, conforme Art. 363 da IN Pres/INSS nº 28/2022:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33699990945943)

Exemplo de Parametrização:   
Cadastro do Dependente idade igual a 13 anos e o campo "Entregou comprov. frequência escolar" marcado. Conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33700052555927)

Geração do XML S-2205:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33700052559895)

Saiba mais:

[Salário Família - Declaração de frequência escolar a partir de 4 anos](https://tdn.totvs.com/pages/releaseview.action?pageId=860252085)
