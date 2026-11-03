---
article_id: 35278948195351
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 7caf42126d6fa96e339f5eef22246c3787f3da781aab0266222c83fdb8c02389
fetched_at: '2026-06-28T22:39:08.021716+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Alteração no tamanho
  de campos NUMSEQ
type: support-article
updated_at: '2026-01-08T22:25:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35278948195351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Altera%C3%A7%C3%A3o-no-tamanho-de-campos-NUMSEQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35278964549015) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**

Ajuste/alteração no tamanho dos campos NUMSEQ

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2410 ou Superior.  
  
**Causa**

Mesmo sendo um campo alfanumérico de 6 posições, o **NUMSEQ** pode ter suas combinações esgotadas em alguns cenários, resultando em duplicações após o reinício. Nesses casos, pode ser necessário ajustá-lo manualmente para permitir a geração de novos códigos.

**Solução**  
Abaixo seguem alguns pontos de atenção para esse tipo de alteração

1. **Campos envolvidos**  
   Caso a numeração tenha por atingir o valor máximo do campo (ZZZZZZ). Os principais campos envolvidos no processo estão listados na documentação: 

   ## [**Campos envolvidos no controle de numeração NUMSEQ**](https://tdn.totvs.com/display/PROT/Tabelas+e+campos+envolvidos)
2. **Ajuste de Chave @@@SD2**  
   Neste caso, também é necessário realizar um ajuste no controle de numeração, conforme indicado na documentação:  
     
   1. Acessar o controle de numeração do configurador  
     
   2. Localizar a chave que faz o controle da numeração NUMSEQ; a chave tem o formato SpecialKey + @@@ + SD2 + Código da empresa + 0. Por exemplo, PROD@@@SD2010 (**O alias da chave será sempre SD2**)  
     
   3. Ao localizar a chave, alterar o tamanho e a numeração, conforme novo tamanho de campos NUMSEQ. Por exemplo, se o campo foi alterado de tamanho 6 para 10, deve-se alterar o campo “Tamanho” de 6 para 10 e o campo “Numero” de 003409 para 0034090000.  
     
   4. Avaliar o grid Números em uso/Números liberados, e ajustar quaisquer numerações não confirmadas lá também.
3. **Mais de um ambiente apontando para o mesmo banco de dados**  
   Se houver mais de um ambiente configurado sem a *SpecialKey* (ou com {*}CheckSpecialKey = 0{*}), a sequência pode ser impactada por movimentações da homologação, gerando duplicidades ou saltos na numeração.  
     
   Em empresas onde existem mais de um ambiente apontando para o mesmo banco de dados, com chaves {*}SpecialKey diferentes{*}, podem ocorrer problemas similares, pois o License Server fará o controle paralelo de várias numerações para gravar a mesma tabela.

   [**A chave CheckSpecialKey em seu ambiente está desligada, você deve liga-la para seu uso da seção [GENERAL]**](https://informa.totvs.com/backoffice/urgente-atualizacao-obrigatoria-no-sistema-ativacao-da-chave-checkspecialkey/)

**IMPORTANTE:** O sistema agora impede a execução das rotinas se detectar configuração incorreta da {*}SpecialKey{*}, evitando que o problema se propague. Dados já gravados devem ser ajustados manualmente.

### **Realizei os ajustes e a Sequência da Numeração ainda estão sendo criadas incorretamente. O que Fazer?**

Para esse cenário **verificar se é o caso** reportado na FAQ abaixo:

[**SIGAEST - Campos \_NUMSEQ repetidos mesmo após apagar lsnumber.val e reiniciar o License Server**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36253990471191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campos-NUMSEQ-repetidos-mesmo-ap%C3%B3s-apagar-lsnumber-val-e-reiniciar-o-License-Server)

***Saiba mais:***

[Descontinuidade do MV\_DOCSEQ na Release 12.1.2410](https://tdn.totvs.com/pages/viewpage.action?pageId=840763998)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Salto de numeração ou registros duplicados no NUMSEQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33294983047063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Salto-de-numera%C3%A7%C3%A3o-ou-registros-duplicados-no-NUMSEQ)

[Cross Segmentos - Backoffice Protheus - SIGAFAT - A chave CheckSpecialKey em seu ambiente está desligada, você deve liga-la para seu uso da seção [GENERAL]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34672116970519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-A-chave-CheckSpecialKey-em-seu-ambiente-est%C3%A1-desligada-voc%C3%AA-deve-liga-la-para-seu-uso-da-se%C3%A7%C3%A3o-GENERAL)

[SIGAEST - Campos \_NUMSEQ repetidos mesmo após apagar lsnumber.val e reiniciar o License Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36253990471191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campos-NUMSEQ-repetidos-mesmo-ap%C3%B3s-apagar-lsnumber-val-e-reiniciar-o-License-Server)

[SIGAEST - Erro no calculo do custo \_NUMSEQ duplicado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35855256093207/live_preview/01K9T5D6HYGTPTV8H9D65NSVH1)
