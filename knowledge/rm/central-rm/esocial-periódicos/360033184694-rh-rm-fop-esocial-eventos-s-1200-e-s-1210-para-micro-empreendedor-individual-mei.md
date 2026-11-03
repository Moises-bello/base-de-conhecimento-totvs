---
article_id: 360033184694
category: esocial - Periódicos
content_hash: babc0ac3c8ed8b180984adac261d8302ff68ed1c3093fdb538ecb90f1fd4a05c
fetched_at: '2026-06-28T22:47:09.381772+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Eventos S-1200 e S-1210 para micro empreendedor individual
  (MEI) do RM Labore
type: support-article
updated_at: '2024-11-25T17:50:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033184694-RH-RM-FOP-eSocial-Eventos-S-1200-e-S-1210-para-micro-empreendedor-individual-MEI-do-RM-Labore
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24456032414359) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**  
Como gerar os eventos **S-1200** e **S-1210** na contratação de **MEI** - categoria 741, registrado no TOTVS Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - A partir da versão 12.1.23  
  
**Solução**  
Conforme o **Manual de Orientação do eSocial**, na contratação de **MEI** - Microempreendedor Individual, quando este prestar serviços de hidráulica, eletricidade, pintura, alvenaria, carpintaria e de manutenção ou reparo de veículos, a pessoas jurídicas, o contratante deverá enquadrá-lo na categoria **741** da **Tabela 1** **– Categoria de Trabalhadores**. Neste caso, o **MEI** deve ser tratado como contribuinte individual, **sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado**, e **ser identificado pelo CPF e NIS**. Nos demais casos de contratação de **MEI** por pessoa jurídica, o contratante nada informará no eSocial.

Considerando as informações acima, siga os seguintes passos para a correta geração dos eventos:  
1. Em **Administração de Pessoal | Funcionários**, verifique se na aba **Registro** o campo **Código da Categoria eSocial** está preenchido corretamente com o valor **741**. O **S-2300** deste funcionário deve ter sido enviado com esta categoria;  
2. No envelope de pagamento, lance a remuneração do funcionário com uma verba que não incida em INSS;  
3. Acesse **eSocial | Gerar XML** (Eventos Periódicos) e execute o processo para o período de apuração desejado selecionando os eventos **S-1200** e **S-1210**;

Os eventos apresentarão o código de categoria **741** na tag **codCateg**.  
  
**Saiba mais**  
Veja mais detalhe em [Eventos de S-1200 e S-1210 na contratação de MEI - Microempreendedor Individual - Autônomos cadastrados na Folha de Pagamento](http://tdn.totvs.com/pages/releaseview.action?pageId=417696032).
