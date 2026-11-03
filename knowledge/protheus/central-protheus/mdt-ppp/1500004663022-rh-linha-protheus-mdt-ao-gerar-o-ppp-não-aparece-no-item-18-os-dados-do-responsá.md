---
article_id: 1500004663022
category: MDT - PPP
content_hash: 17e8edecc086982251a2e5a03e2114eb3b959db1e10e5e0e05ddc8ba30d780a0
fetched_at: '2026-06-28T22:44:22.191420+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus -  MDT - Ao gerar o PPP não aparece no item 18 os dados
  do responsável pela monitoração biológica
type: support-article
updated_at: '2023-12-26T18:05:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004663022-RH-Linha-Protheus-MDT-Ao-gerar-o-PPP-n%C3%A3o-aparece-no-item-18-os-dados-do-respons%C3%A1vel-pela-monitora%C3%A7%C3%A3o-biol%C3%B3gica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20029725204759)**  Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao gerar o PPP não aparece no item 18 os dados do **responsável pela monitoração biológica**.   
  
**Ambiente**TOTVS RH (Linha Protheus) -  Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Isso pode ocorrer devido as seguintes causas:

1. Não existe usuário do sesmt com o campo **Monit. Biolog.** (TMK\_MONBIO) preenchido com **SIM** na rotina Sesmt/usuar.aten. (MDTA070);  
2. O campo **centro de custo** está preenchido a rotina Sesmt/usuar.aten. (MDTA070), porem o trabalhador que está sendo gerado no PPP pertence a um centro de custo diferente do usuário do sesmt;  
3. Não existe usuário do sesmt com a função de **Técnico de Segurança do Trabalho** ou **Médico do Trabalho**.  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte:  
[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)  
Estas informações são obtidas da tabela de componentes do **SESMT** (TMK). O programa irá considerar todos os componentes que estiverem com o campo “**Função**” selecionado para Técnico de Segurança do Trabalho ou Médico do Trabalho.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse no modulo 35 (SIGAMDT) o caminho: **Atualizações > Sesmt > Sesmt/usuar.aten.** (MDTA070). E verifique os campos:

* **Função**: Deve ser Técnico de Segurança do Trabalho ou Médico do Trabalho;
* **Centro de Custo**: Deve deixar em branco se quiser que o usuário Sesmt apareça no PPP de qualquer trabalhador independente do centro de custo em que ele está;
* **Campo Monit. Biolog. (TMK\_MONBIO)**: Deve ficar com SIM.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006144661)  
  
2.  Acesse no modulo 35 (SIGAMDT) o caminho: **Atualizações > Relatórios > PPP > Perfil Profissiogr** (MDTR700), e na definição dos parâmetros defina as perguntas **Imp. Resp. Monit. Biologica** e **Função**.  
  
![responsavel_monitoracao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006144741)  
  
3. Confirme a geração do relatório de PPP (MDTR700) e verifique o quadro 18.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006144861)  
 **Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
