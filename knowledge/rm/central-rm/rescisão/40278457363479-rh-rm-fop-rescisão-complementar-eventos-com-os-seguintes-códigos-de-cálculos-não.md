---
article_id: 40278457363479
category: Rescisão
content_hash: a75d5226e578f27f7efd039bbc51cf0cda505863610b0ea32a72335ac02f3989
fetched_at: '2026-06-28T22:46:54.122148+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão Complementar: Eventos com os seguintes códigos de
  cálculos não foram localizados'
type: support-article
updated_at: '2026-05-07T14:41:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40278457363479-RH-RM-FOP-Rescis%C3%A3o-Complementar-Eventos-com-os-seguintes-c%C3%B3digos-de-c%C3%A1lculos-n%C3%A3o-foram-localizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40278457311639) Tempo aproximado para leitura: **00:02:55 min**  
  
**Dúvida**  
Ao realizar um lançamento de diferença salarial na rescisão complementar, o sistema apresenta a mensagem "ERRO: Inconsistência no cálculo da Rescisão Complementar. Eventos com os seguintes códigos de cálculos não foram localizados: 63", mesmo que o lançamento não tenha relação com férias.

**Ambiente**  
TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O erro ocorre porque o motor de cálculo da rescisão complementar exige a existência de um evento configurado com o Código de Cálculo 63 (1/3 de Férias Rescisão) na coligada. Mesmo que não haja valores de férias a serem pagos no movimento em questão, o sistema valida a existência deste código para a correta estruturação do cálculo.

Para solucionar essa dúvida, realize os seguintes passos:

1.  Acesse:**Administração de Pessoal | Eventos | Eventos**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40278444953239)

2. Clique no ícone de inclusão para cadastrar um novo evento, conforme a imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40278457314711)

3. No campo **Código de Cálculo**, informe 63 (1/3 de Férias Rescisão), No campo **Prov/Desc/Base**, selecione a opção Provento, No campo **Val/Hor/Dia/Ref**, selecione a opção Valor, conforme o exemplo da imagem abaixo.

Observação: Na aba Inc. Proventos, certifique-se de configurar a incidência em IRRF Férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40278444957719)

**Saiba mais**

[Códigos de Cálculo](https://C%C3%B3digos%20de%20C%C3%A1lculo)

[Eventos de Cálculo](https://Eventos%20de%20C%C3%A1lculo)
