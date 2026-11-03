---
article_id: 360058050253
category: MDT - eSocial
content_hash: 3acd8d64bae6f2f8dad775f0fc31c4a0516d09784bc5ea2ce690dafae650896a
fetched_at: '2026-06-28T22:44:29.332647+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Aviso os campos abaixo são importância
  para a consistência das informações que serão enviadas ao eSocial! Ent. Classe,
  Num.Ent.Cl., e UF Ent
type: support-article
updated_at: '2025-08-05T17:05:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058050253-RH-Linha-Protheus-MDT-eSocial-Aviso-os-campos-abaixo-s%C3%A3o-import%C3%A2ncia-para-a-consist%C3%AAncia-das-informa%C3%A7%C3%B5es-que-ser%C3%A3o-enviadas-ao-eSocial-Ent-Classe-Num-Ent-Cl-e-UF-Ent
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372181815191)**Tempo aproximado para leitura**: 00:02:00 min****Ocorrência**Ao tentar cadastrar um medico ocorre a mensagem: Aviso os campos abaixo são importância para a consistência das informações que serão enviadas ao eSocial! **Ent. Classe**, **Num.Ent.Cl.**, e **UF Ent.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097681533)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem pode ocorrer sempre que o parâmetro **MV\_NG2ESOC** estiver com **1** para que seja possível a integração com o TAF. Conforme layout do eSocial, as informações de **Ent. Classe**, **Num.Ent.Cl.**, e **UF Ent.** são obrigatórias em vários eventos. Para que não exista problemas no envio dos eventos é necessario preencher esses campos.   
  
Abaixo destaco exemplo do layout onde a informação é utilizada.

* [S-2210 - Comunicação de Acidente de Trabalho](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-01-2021-html/index.html/index.html#evtCAT)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403547859479)

* [S-2220 - Monitoramento da Saúde do Trabalhador](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-01-2021-html/index.html/index.html#evtMonit)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403554675991)

* [S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-01-2021-html/index.html/index.html#evtExpRisco)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403554823959)  
  
**Solução**  
Para ajuste é necessario cadastrar o medico na rotina **SESMT/Usuar.aten. (MDTA070)** localizada no Módulo 35 (SIGAMDT) no caminho: Atualizações - Sesmt - Sesmt/usuar.aten. Nos casos em que a mensagem ocorre na geração da CAT ou Atestado deve ser verificado se o medico emitente também está devidamente cadastrado no caminho: Atualizações - Atendimento Médico - Médico Emitente de Atestado **(****MDTA680).**  
  
**Observação**  
[RH - Linha Protheus - MDT - Qual a diferença entre a rotina SESMT/Usuar.aten. (MDTA070) e a rotina Emitentes de Atestados (MDTA680) no modulo medicina e segurança do trabalho (SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056925334)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
