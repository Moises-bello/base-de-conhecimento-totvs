---
article_id: 4403421565335
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 8ed0b2e4ef9c5fc5742167b9b9c14bb50422d952791609152f6d1c75590188f3
fetched_at: '2026-06-28T22:42:04.948500+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como excluir
  o ICMS a Recolher e Como excluir o ICMS Destacado no EFD Contribuições
type: support-article
updated_at: '2023-05-26T12:14:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403421565335-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-excluir-o-ICMS-a-Recolher-e-Como-excluir-o-ICMS-Destacado-no-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como excluir o ICMS a Recolher e Como excluir o ICMS Destacado no EFD Contribuições?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**A exclusão pode ser tratada das duas formas:  
  
Opção 01 - **Exclusão do ICMS Destacado:**Nesta hipótese o contribuinte possui processo judicial que permite a exclusão do ICMS destacado na nota fiscal. Desta forma base de cálculo de PIS e COFINS já possui a exclusão do ICMS diretamente no cálculo da nota fiscal, ou seja, o valor de PIS e COFINS já é calculado considerando a exclusão do ICMS.

Em resumo, a composição da base de cálculo na apuração da EFD Contribuições não possui o valor de ICMS, pois já foi excluído diretamente no cálculo da nota fiscal, logo não haverá ajustes de base de cálculo na EFD Contribuições.

Para solucionar essa dúvida, realize os seguintes passos:  
1. Configure os parâmetros **MV\_DEDBPIS = I** e **MV\_DEDBCOF= I**  
2. Lance a Nota Fiscal e verifique se a base de cálculo do **PIS** e **COFINS** se já está descontando o **ICMS**;  
3. Confira os valores gravados nos campos **FT\_BASEPIS,** **FT\_BASECOF,** **FT\_VALPIS,** **FT\_VALCOF,** **FT\_ALIQCOF e** **FT\_ALIQPIS**, antes de gerar o arquivo do EFD Contribuições esses campos devem estar corretos.

Opção 02 - **Exclusão do ICMS a Recolher:**

Nesta hipótese o contribuinte possui processo que permite a exclusão do ICMS a recolher obtido da apuração de ICMS, que é declarado na família do registro **E100** do **SPED Fiscal**. Nesse caso, os valores de PIS e COFINS são calculados na nota fiscal **sem excluir** **o****ICMS destacado**, e somente serão excluídos da base de cálculo na apuração da EFD Contribuições, considerando o ICMS a recolher, que é resultado da apuração de ICMS.

Em resumo, a composição da base de cálculo na apuração da EFD Contribuições terá o valor de ICMS dentro da base de cálculo, pois não foi excluído na nota fiscal, e neste caso ocorrerá a exclusão do ICMS a Recolher da base de cálculo de PIS e COFINS no processo de apuração da EFD Contribuições, através dos ajustes de redução da base de cálculo.

Os parâmetros precisam estar conforme abaixo, no momento da escrituração do documento:  
  
Para solucionar essa dúvida, realize os seguintes passos:

1. Configure os parâmetros **MV\_DEDBPIS= N**, **MV\_DEDBCOF= N** e **MV\_USASPED = .T.**  
2. Processe a **Apuração do ICMS**  
Importante lembrar que para este cálculo é necessário processar **Apuração de ICMS** com o parâmetro **MV\_USASPED** com conteúdo igual a .T., caso contrário a **Apuração da EFD Contribuições** não conseguirá obter o valor de **ICMS a recolher** no período.  
3. Acesse a **Rotina FISA001** e processe a **Apuração do EFD Contribuições,** atente-se a pergunta **Livro: ?** preencha com asterisco ( \* ), para a Rotina buscar a movimentação de todos os Livros.4. Atente-se a pergunta da *Wizard* **Decisão Judicial Ex. ICMS ?** Marque a opção **ICMS a Recolher**![imagem_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403422006039/imagem_1.png)  
  
5. Atente-se a pergunta **Exclusão ICMS a Recolher ?** Marque a opção **Rec. Suj. ICMS** se deverá ser tratado para fazer o calculo referente os **Blocos C e D** por **CST**, já que esses blocos, possuem incidência do **ICMS**.  
O sistema não verifica apenas as notas que tiveram **ICMS**, mas sim o que foi tributado sim ou não do **ICMS**. O sistema busca os **Blocos C e D** com o valor total da Receita por **CST**.  
A opção **Total Receita**, faz o processo em todos os blocos do EFD Contribuições, ou seja total de todas as Receitas.  
  
![imagem_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403427344663/imagem_2.png)​  
  
Importante: A geração da **Apuração e Arquivo EFD**, deve ser gerada pela **empresa Matriz**, selecionando as empresas desejadas, incluindo a Matriz.  
  
Link completo da documentação da Apuração:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>   
  
Link completo da documentação do Arquivo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=212895074>

Link referente a Operacionalização dos ajustes de exclusão do ICMS da base de cálculo do PIS/Cofins  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=628632309>

Para o preenchimento automático dos complementos a serem demonstrados no arquivo txt do **EFD Contribuições**, configure o **Ponto de Entrada MATUCOMP**.  
  
Link: <https://tdn.totvs.com/pages/releaseview.action?pageId=6077107>
