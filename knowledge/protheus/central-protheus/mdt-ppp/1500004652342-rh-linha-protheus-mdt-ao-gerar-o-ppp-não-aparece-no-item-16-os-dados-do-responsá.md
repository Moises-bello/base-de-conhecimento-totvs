---
article_id: 1500004652342
category: MDT - PPP
content_hash: 1d9370b032ab07b4088bcc09b6cdf8b774395573047cd10e947a23ea32f3c7c5
fetched_at: '2026-06-28T22:44:22.180554+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus -  MDT - Ao gerar o PPP não aparece no item 16 os dados
  do responsável pelos registros ambientais
type: support-article
updated_at: '2023-12-26T18:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004652342-RH-Linha-Protheus-MDT-Ao-gerar-o-PPP-n%C3%A3o-aparece-no-item-16-os-dados-do-respons%C3%A1vel-pelos-registros-ambientais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20117141950615)**Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao gerar o PPP não aparece no item 16 os dados do **responsável pelos registros ambientais**.   
  
**Ambiente**TOTVS RH (Linha Protheus) -  Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Isso pode ocorrer devido as seguintes causas:

1. Não existe usuário do sesmt com o campo **Resp. Amb.** (TMK\_RESAMB) preenchido com **SIM** na rotina Sesmt/usuar.aten. (MDTA070);  
2. O campo **centro de custo** está preenchido a rotina Sesmt/usuar.aten. (MDTA070), porem o trabalhador que está sendo gerado no PPP pertence a um centro de custo diferente do usuário do sesmt;  
3. Não existe usuário do sesmt com a função de **Engenheiro de Segurança do Trabalho** ou **Médico do Trabalho**.  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte:  
[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)  
Estas informações são obtidas da tabela de componentes do **SESMT** (TMK). O programa irá considerar todos os componentes que estiverem com o campo “**Função**” selecionado para Engenheiro de Segurança do Trabalho ou Médico do Trabalho.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse no modulo 35 (SIGAMDT) o caminho: **Atualizações > Sesmt > Sesmt/usuar.aten.** (MDTA070). E verifique os campos:

* **Função**: Deve ser Engenheiro de Segurança do Trabalho ou Médico do Trabalho;
* **Centro de Custo**: Deve deixar em branco se quiser que o usuário Sesmt apareça no PPP de qualquer trabalhador independente do centro de custo em que ele está;
* **Campo Resp. Amb. (TMK\_RESAMB)**: Deve ficar com SIM.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006130801)  
  
2.  Acesse no modulo 35 (SIGAMDT) o caminho: **Atualizações > Relatórios > PPP > Perfil Profissiogr** (MDTR700), e na definição dos parâmetros defina a pergunta **Responsável Ambiental**.  
![responsavel_ambiental.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006020722)  
  
3. Confirme a geração do relatório de PPP (MDTR700) e verifique o quadro 16. ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006133821)  
  
**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
