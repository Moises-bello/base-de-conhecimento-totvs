---
article_id: 360051658173
category: RH - Leitura e Apontamento
content_hash: 025736d29d3bc51ed70790d1aa1ec82d941b28a5afc837cac1929b7899e8385b
fetched_at: '2026-06-28T22:44:45.970474+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Leitura e apontamento gera divergência de NSR
type: support-article
updated_at: '2025-06-13T17:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051658173-RH-Linha-Protheus-PON-Leitura-e-apontamento-gera-diverg%C3%AAncia-de-NSR
---

**Ocorrência**Ao executar a Leitura/Apontamento, o sistema gera log informando divergências de NSR, não gravando as marcações do arquivo TXT.  
**Arquivo C:\PONTO\XXXX\XXXX.TXT com marcações divergentes**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080012573)  
   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa  
1.** Quando o Relógio de Ponto passa por **reparo técnico**, a sequência de NSR é **zerada**, ou seja, a sequência começa a ser contada novamente a partir do NSR 000000001 como se fosse um relógio novo;  
**2.** O próprio REP físico, por algum problema interno ou configuração incorreta, realiza um "*restart*" na sequência do NSR.  
  
**Solução  
1.** Cadastre este relógio novamente no Protheus como se fosse um novo equipamento;  
**2.** O cadastro anterior não deve ser apagado por conta do histórico;  
**3.** É recomendado sempre utilizar um **Código de relógio** no Protheus com **3 posições** (exemplo 010 e não 10), bem como para este novo REP cadastrado, utilizarmos um novo nome de arquivo.txt.  
  
**Saiba mais:**[MP - PON - Como efetuar o cadastro do Relógio Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-MP-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-Ponto?source=search)  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
