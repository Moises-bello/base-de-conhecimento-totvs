---
article_id: 360020040531
category: ADVPL - Ponto de Entrada
content_hash: 0f86ecbcd7f328e40f7693e1280580692dc6763ad26d3cbd46a48de31443850c
fetched_at: '2026-06-28T22:40:11.789273+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  CALLCHGXNU '
type: support-article
updated_at: '2021-12-29T15:08:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020040531-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-CALLCHGXNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**O ponto de entrada **CALLCHGXNU** está passando parâmetro errado para ser executado, ele não envia a empresa e filial nova digitada pelo usuário, está enviando a empresa e filial posicionada, deveria ser passada a nova, pois o ponto de entrada é para troca de Menu (para nova conexão) e não para conexão antiga.   
o problema ocorre na troca de módulo ou empresa clicando na faixa superior ou no nome do módulo, usando **SIGAMDI** OU **SIGAADV**  o primeiro acesso funciona OK.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**De acordo com a documentação para que seja exibido através de **MsgAlert**,**Alert** ou qualquer outro método que possibilite exibir a Empresa, Filial é necessário utilizar o **ParamIXB**[6] e **ParamIXB**[7] após a primeira carga.

```
ParamIXB[6] (Caracter) -> Empresa selecionada de destino. (Na primeira carga do sistema será a mesma empresa do parâmetro ParamIXB[2] )  
  
ParamIXB[7] (Caracter) -> Filial selecionada de destino.(Na primeira carga do sistema será a mesma filial do parâmetro ParamIXB[3] )
```

**Observação:**

Ele somente envia grupo de empresas e filial diferente da logada ao trocar de grupo de empresas no sistema (pela tela do MDI, por exemplo).

Não executa como administrador

Com **dicionário no banco de dados** este ponto de entrada deve retornar o **id do menu** e não o seu nome antigo.

**Saiba Mais****[CALLCHGXNU](http://tdn.totvs.com/display/PROT/CALLCHGXNU)**
