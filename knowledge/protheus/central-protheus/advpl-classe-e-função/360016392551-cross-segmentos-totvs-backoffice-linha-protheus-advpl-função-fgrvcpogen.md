---
article_id: 360016392551
category: ADVPL - Classe e Função
content_hash: f72ee44b0c139ac61f63309a977e3674e80450b8895cfbc0f28c14e0cc5ffec0
fetched_at: '2026-06-28T22:40:19.343314+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função FGrvCpoGen
type: support-article
updated_at: '2022-01-10T18:40:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016392551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-FGrvCpoGen
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Quando utilizado o ponto de entrada **MNTA7161** para validar os registros que serão importados pela rotina de **Importação de Abastecimento** (MNTA716) com base no **Layout de Importação** (MNTA715), nota-se que a mesma está duplicando registros no vetor aTR6Incl (passado via PARAMIXB).

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012187312/Sem_t_tulo.png)

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**A função **FGrvCpoGen()** foi criada com o intuito de preparar os valores importados para uma possível recolocação em campos de tabela.  
  
**Solução**Remover a função do campo **TQ8\_FUNCAO** em casos onde o campo informado já exista no banco de dados.  
  
**Exemplo**  
*"O arquivo de abastecimento enviado pelo meu fornecedor contém alguns campos que eu não utilizo atualmente, contudo, podem me ser úteis no futuro"*.

Em casos como este utiliza-se a função **FGrvCpoGen()** para preparar os campos para utilização em campos de tabela.  
Note no layout abaixo que os campos que utilizam a função, não são campos reais (presentes no banco), mas recebem na função como uma espécie de "preparação" para serem inseridos futuramente em campos reais.

![d.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012182511/d.png)

**Saiba mais**[Como configurar as funcoes de validacao do mnta715 e mnta716](http://tdn.totvs.com/display/PROT/MNT0026_Como_configurar_as_funcoes_de_validacao_do_mnta715_e_mnta716)  
[Como alterar os layout padrão de importação de abastecimento](http://tdn.totvs.com/display/PROT/MNT0074+Como+alterar+o+layout+padrao+da+importacao+de+abastecimento)  
[MNTA7161 - Realiza verificação por linha se deve importar os registros de abastecimentos](http://tdn.totvs.com/display/PROT/DT+PE+MNTA7161+Verifica+por+linha+se+deve+realizar+a+importacao+de+abastecimento)
