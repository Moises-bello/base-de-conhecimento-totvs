---
article_id: 360016519791
category: RH - 13º salário
content_hash: 134fa7b144d271f2566bda969a77202ca7f28c4fca6260bc2512b97293bb9728
fetched_at: '2026-06-28T22:44:00.596367+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o sistema para gerar automaticamente
  valores de complemento de 13º Salário
type: support-article
updated_at: '2026-01-08T10:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519791-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-gerar-automaticamente-valores-de-complemento-de-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17900693870615) Tempo aproximado para leitura: 00:003:00 min  
  
Dúvida**Como configurar o sistema para gerar automaticamente valores de diferença de 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que seja calculada a diferença de 13º, é necessário as seguintes configurações:  
  
1. Mnemônico **P\_CCOMP13** deve estar com conteúdo **"S"** (em aspas duplas);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34298261350551)  
  
2. O parâmetro **MV\_DF13NEG** deve estar habilitado, caso queria calcular diferença negativa (exemplo ao final da documentação);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34298245171991)  
  
3. Possuir as verbas de **id 0028 e 0348** cadastradas, com incidência **Sim** para **Ref. 13º**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34298261353495)  
  
  
**Observações:**-A diferença é paga na Folha, para isso o **roteiro 132** deve estar **calculado e** **fechado** (esta rotina não possui integração);-Se a verba de Diferença for configurada com **Sim** para 13º, as diferenças serão calculadas sobre as bases de INSS, IR e FGTS de 13º, **separados** dos encargos da folha.  
-Se a verba de Diferença for configurada com **Não** para 13º, as diferenças serão calculadas sobre as bases de INSS, IR e FGTS da folha normal. 

**Exemplo de Diferença Positiva**   
O colaborador recebeu o 13° Salario de 12/12 avos (roteiro 132), sobre um salario de 3.000,00, e no dia 01/12/2024 o seu salário foi aumentado para 3.500,00  
O sistema calculou na competência 12 (roteiro FOL), a diferença de 500,00 e todos os encargos relativos a 13° Salario.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34298245173655)

**Exemplo de Diferença Negativa**O colaborador recebeu no início do mês de Dezembro o 13º Salário considerando 12/12 avos, mas teve um afastamento que fez com que o avo de Dezembro fosse indevido.  
O sistema realizou a devolução dos valores referente a INSS e FGTS nos ids 1672, 1673, 1676, 1677, e no ID 0348 descontou o avo pago a maior.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34298261355287)  
  
 **Saiba Mais**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)[RH - Linha Protheus - GPE - Conferência do Complemento de 13º Salário na Folha de Dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061244313-RH-Linha-Protheus-GPE-Confer%C3%AAncia-do-Complemento-de-13%C2%BA-Sal%C3%A1rio-na-Folha-de-Dezembro?source=search)  
[RH - Linha Protheus - GPE - Cálculo de Complemento de 13º salário na Folha de Dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019750511-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Complemento-de-13%C2%BA-sal%C3%A1rio-na-Folha-de-Dezembro?source=search)  
[RH - Linha Protheus - GPE - Complemento 13º negativo impede a transmissão do S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332213-RH-Linha-Protheus-GPE-Complemento-13%C2%BA-negativo-impede-a-transmiss%C3%A3o-do-S-1200?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIikwZjY0ZTBhNS0wM2QzLTQwYzItYTk4Zi01YzcyODhhYTQ1MzkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--c706b14ad410ef4e30990fb67007ceb534a66c73)
