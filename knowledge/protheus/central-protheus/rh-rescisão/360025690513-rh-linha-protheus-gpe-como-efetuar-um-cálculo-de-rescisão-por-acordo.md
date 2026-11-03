---
article_id: 360025690513
category: RH - Rescisão
content_hash: e4daa0d0cae712d468e2fda9a2dfc21af98eedcb356d6e0f7840c17e312c8c67
fetched_at: '2026-06-28T22:43:48.666925+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar um cálculo de rescisão por acordo
type: support-article
updated_at: '2025-07-14T19:07:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025690513-RH-Linha-Protheus-GPE-Como-efetuar-um-c%C3%A1lculo-de-rescis%C3%A3o-por-acordo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33462447907735) Tempo aproximado para leitura:**00:04:00 min**

**Dúvida**Como efetuar um cálculo de rescisão por acordo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução***Art. 484-A. O contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas:*  
*I – por metade:*  
*a) o aviso prévio, se indenizado; e*  
*b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº 8.036, de 11 de maio de 1990;*  
*II – na integralidade, as demais verbas trabalhistas.*  
*§ 1º A extinção do contrato prevista no caput deste artigo permite a movimentação da conta vinculada do trabalhador no Fundo de Garantia do Tempo de Serviço na forma do inciso I-A do art. 20 da Lei nº 8.036, de 11 de maio de 1990, limitada até 80% (oitenta por cento) do valor dos depósitos.*  
*§ 2º A extinção do contrato por acordo prevista no caput deste artigo não autoriza o ingresso no Programa de Seguro-Desemprego*

Com este acordo o empregado está autorizado a levantar 80% do valor dos depósitos do FGTS, mas não terá direito a receber o seguro-desemprego (art. 484-A, CLT; art. 20, inciso I-A da Lei n. 8.036/90).  
  
Passos:  
**1.  Crie um tipo de rescisão por ACORDO na tabela S043**

\*\*É de responsabilidade da empresa definir as configurações dos campos do tipo de rescisão com as informações que devem ser calculadas na rescisão.

Foi criado o tipo de aviso prévio “A” para no momento do cálculo de rescisão o sistema calcular 50% dos dias de aviso. Exemplo: se o funcionário estiver na empresa por 4 anos, ele teria direito a 42 dias (30 + 12 = 42) de aviso prévio se fosse uma rescisão diferente de comum acordo. No caso de comum acordo serão calculados 21 dias (42 \* 50% = 21).

 Configure o % de FGTS com 20%  
Informe código de afastamento FGTS = I5  
  
**2. Atualize o sistema com o pacote indicado no link:**[Documento Técnico Reforma Trabalhista Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=311632134)

**3. Execute os procedimentos do documento técnico disponível no link:**  
[Documento Técnico Reforma Trabalhista Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=311632134)

**4: Processo de cálculo. Acesse a tabela S043 (P12) ou Parâmetro 32 (P11) para conferir as configurações do tipo de rescisão: ACORDO**

P11 - Em Atualizações > Definições de Calculo > Parâmetros > Parâmetro 32  
P12 - Em Atualizações > Definições de Calculo > Manutenção de tabelas > Tabela S043 - Tipos de Rescisão![](http://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-9-19.png?version=1&modificationDate=1518433760000&api=v2)![](http://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-10-15.png?version=1&modificationDate=1518433816000&api=v2)

**OBS: Na versão 11, o campo "Cód. Afast. FGTS" deve permanecer apenas com o conteúdo I. Internamente, pelo campo "Aviso Prévio", o qual está configurado com A (Acordo) é que o sistema levará o código I5 na GRRF**

* + Não será gerada a verba de contribuição social referente a multa de 10% (id 0297) quanto tipo de aviso for "A";
  + Cadastro de tipo de rescisão (S043) no campo Cod. Homolognet permitirá o cadastro "em branco";
  + TRCT campo 22 deverá constar com "Acordo Empregado e Empregador" - Essa informação vem da tabela S043;
  + TRCT campo 27 deveria constar "em branco " - Essa informação vem da tabela S043(cod. Homolognet).

Necessário acessar o menu Atualizações> Definições de Tabelas para que atualize a estrutura da tabela S043 e após isso acessar Manutenção de tabelas e preencher os campos Descrição e Cod. Homolognet corretamente.

**Patch de adequação: [DRHPAG-9580 DT Reforma Trabalhista - Adequação no cálculo de rescisão por comum acordo](http://tdn.totvs.com/pages/viewpage.action?pageId=322151751)**

Cálculo de rescisão:![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-21_18-7-49.png?version=1&modificationDate=1511294870000&api=v2)

O sistema calculou metade dos dias dias aviso conforme legislação e valor da multa do FGTS reduzida a 20%![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-37-25.png?version=1&modificationDate=1511357846000&api=v2)

TRCT:

![](http://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-15-50.png?version=1&modificationDate=1518434150000&api=v2)

**5. Geração da GRRF**

![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-41-30.png?version=1&modificationDate=1511358090000&api=v2)![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-41-44.png?version=1&modificationDate=1511358105000&api=v2)![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-42-7.png?version=1&modificationDate=1511358127000&api=v2)

![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-42-26.png?version=1&modificationDate=1511358147000&api=v2)

![](http://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-40-55.png?version=1&modificationDate=1511358056000&api=v2)  
  
**IMPORTANTE:** É necessário que os programas da GRRF e da SEFIP estejam atualizados

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
