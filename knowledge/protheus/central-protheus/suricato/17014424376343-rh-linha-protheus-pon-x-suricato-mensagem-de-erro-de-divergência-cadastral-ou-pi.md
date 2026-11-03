---
article_id: 17014424376343
category: Suricato
content_hash: bffb909e42cb9afcbe60416ac4d4bad1bfa603694666404a0bb7d0cefed122c4
fetched_at: '2026-06-28T22:44:57.295251+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Mensagem de erro de divergência cadastral
  ou PIS na leitura de marcações vindas do Suricato
type: support-article
updated_at: '2025-10-07T16:44:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17014424376343-RH-Linha-Protheus-PON-x-Suricato-Mensagem-de-erro-de-diverg%C3%AAncia-cadastral-ou-PIS-na-leitura-de-marca%C3%A7%C3%B5es-vindas-do-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17014381388823) Tempo aproximado para leitura: **00:05:00 min****Dúvida**O que causa o erro no log da leitura/apontamento de marcações vindas do Suricato: **Há marcações sem preenchimento de PIS/informação cadastral do funcionário ou que não foi possível encontrar o funcionário com a identificação no cadastro de funcionários. Essas marcações não serão importadas para o SIGAPON. IDs das marcações na Tabela**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Se ao executar a **Leitura/Apontamento** de marcações vindas do **Suricato**, for exibido o erro abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468265476119)  
  
Significa que existe algum **erro cadastral** envolvendo os **funcionários ou relógios** listados no log.  
Para localizar quais seriam os funcionários ou relógios, deve ser verificado o **ID da marcação**, que se trata deste código listado. Com este dado, abra a tabela **MSA\_CONTROL\_MARCAC ou RR1**, e busque pelo código no campo **VAL\_CONTROL\_MARCAC ou RR1\_VALCON**, com isso, você poderá ver **através do PIS** qual é o funcionário ou relógio que está com possíveis problemas de cadastro.  
  
Sabendo exatamente quais são os registros, devem ser validados os passos abaixo:  
  
**1.** se o campo **RA\_CRACHA** do cadastro do funcionário está preenchido e exatamente igual ao cadastro do funcionário no Suricato;  
**2.** se o campo **RA\_PIS** do cadastro do funcionário está preenchido e exatamente igual ao cadastro do funcionário no Suricato, e o registro existente na tabela MSA\_CONTROL\_MARCAC ou RR1;  
**3.** se no **cadastro do relógio** que faz integração com o Suricato, o campo **Novo Relógio** (P0\_NOVO) está como **1 - Sim**;  
**4.** verificar se o conteúdo do parâmetro **MV\_TPLMARC** está como **1** para que seja feita a busca pelo PIS.  
  
**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
