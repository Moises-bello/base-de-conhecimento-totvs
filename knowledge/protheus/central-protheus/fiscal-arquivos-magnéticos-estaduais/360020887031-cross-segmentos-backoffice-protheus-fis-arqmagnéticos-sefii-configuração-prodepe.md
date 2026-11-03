---
article_id: 360020887031
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: e3b90b832d40eaf7a3e31f19205011458bd3166b9fb318d364d7ee69f11fdbda
fetched_at: '2026-06-28T22:42:11.854162+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SEFII - Configuração
  Prodepe
type: support-article
updated_at: '2022-08-18T14:13:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020887031-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SEFII-Configura%C3%A7%C3%A3o-Prodepe
---

**Dúvida**Como configurar o beneficio do **Prodepe** para gerar no arquivo **SEFII**  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução****1 -** Configuração do paramêtro **MV\_PROIND** conforme o exemplo:

{{'1','2'}, {'2','3'}, {'3','4'}}

A primeira posição do parâmetro é o livro. A segunda é a sub apuração disponível no layout SEFII.  
No layout diz que a sub apuração 1 é não incentivada e as demais são incentivadas

 Indicador da sub-apuração do Prodepe:  
1- item não incentivado (sub-apuração 1)  
2- item incentivado (sub-apuração 2)  
3- item incentivado (sub-apuração 3)  
...  
\_9- item incentivado (sub-apuração \_9)   
  
No parâmetro NÃO pode-se ter um Livro com o conteúdo em vazio, onde em todas as TES, um livro deve ser configurado para que seja tratado na sub apuração do prodepe.

Exemplo:  
ERRADO: {{'','2'}, {'2','3'}, {'3','4'}}  
CERTO: {{'1','1'}, {'2','2'}, {'3','3'}}

**2 -** Cadastros

TES:   
Produtos incentivados   
Nr. Livro (F4\_NRLIVRO)=   
Crd.PRODEPE (F4\_CPPRODE) = Percentual do incentivo  
Tipo PRODEPE (F4\_TPPRODE)= Tipo de incentivo

TES:  
Produto não incentivados  
Nr. Livro (F4\_NRLIVRO)=  
Crd.PRODEPE (F4\_CPPRODE) = em branco   
Tipo PRODEPE (F4\_TPPRODE)= 0 (sem incentivo)  
  
IMPORTANTE: É obrigatório ter o complemento do produto para todos os produtos que devem compor o arquivo, independente se são ou incentivados.  
  
Produtos incentivados é necessário preencher os campos no complemento de produto:

Complemento de Produto(SB5):  
Natureza do Banefício (B5\_NATBEN) – de acordo com o Layout GI-ICMS – Prodepe;  
Número do Decretro (B5\_NUMBEN);  
Data do decreto concessivo(B5\_DTDECRE);  
Ano de vigência do benefício(B5\_ANOBEN) – prazo de fruição do benef

Para as notas fiscais incentivadas, os campos SFT FT\_TPPRODE e FT\_CPPRODE deverão estar alimentados.

Para as notas fiscais Não incentivadas, apenas o campo FT\_TPPRODE deverá estar preenchido

**3 -**É necessário ter o P9AUTOTEXT.PE na pasta system para que seja criado a linha do Prodepe na apuração;  
Execute a apuração de ICMS para cada livro individualmente e por fim para todos os livros (\*)

**4 -** Wizards para geração do arquivo;  
Selecione o documento a ser gerado for escolhida a opção 4- Prodepe - GI/ICMS,  
Código do conteúdo do arquivo deve ser escolhida a opção 30 - Guia de informações Econômicos Fiscais e declarações,  
Indicador de conteúdo de arquivo deve ser escolhida a opção 7-Guia de informações Econômicos Fiscal.  
  
Mais informações no boletim:   
<http://tdn.totvs.com/display/public/PROT/FIS0024_SEFII>
