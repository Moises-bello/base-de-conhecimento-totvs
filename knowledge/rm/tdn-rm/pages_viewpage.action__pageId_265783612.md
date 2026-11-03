---
content_hash: bfaf90bf4803407c874753d82336a0ae958e68748c0a08729e26f2f1bf371989
fetched_at: '2026-06-29T00:08:18.598562+00:00'
page_id: '265783612'
product: rm
source: tdn-rm
title: Exemplo da utilização de valor monetário Mexicano (Peso Mexicano) com a Biblioteca
  RM Espanhol
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=265783612
version: 1
---

# Utilização de valor monetário mexicano (peso mexicano) com a Biblioteca RM Espanhol

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Utilização de valor monetário mexicano (peso mexicano) com a Biblioteca RM Espanhol |
| **Ambiente:** | MDI |
| **Passo a passo:** | O valor monetário brasileiro é o real, dessa forma, na tabela GPARAMS, os campos Pais e Simbolo moeda são preenchidos, respectivamente com os valores **BRA** e **R$**:    Ao acessar o RM, os valores monetários são apresentados com o separador de milhar "." e de casas decimais "," conforme segue abaixo:    Para que o valor monetário mexicano (peso mexicano) seja apresentado no RM, faz-se necessário a utilização da BibliotecaRM (Español) - 12.1.12.msi.  Os campos Pais e Simbolo moeda na tabela GPARAMS, devem ser cadastrados como **MEX** e **$**, respectivamente:    Caso seja necessária atualização do campo Pais, pode-se utilizar o seguinte comando:  UPDATE GPARAMS SET PAIS ='MEX'  Para alteração do campo Simbolo Moeda, acesse o RM e realize a alteração na aba Gerais:    Na estação, deve-se avaliar as seguintes configurações:  Configurações Regionais:                  Ao instalar a Biblioteca foi selecionado o idioma: Spanish (México), logo nos arquivos de configuração a tag LocalizationLanguage foi setada com o valor es-MX:  <add key="LocalizationLanguage" value="es-MX" />    Após todas as parametrizações, reinicie a máquina e valide o comportamento do RM.  As telas do RM apresentarão os valores no formato selecionado, padrão Mexicano (Ex. 100,000,000.00 (cem milhões)): |
| **Observações:** | **Obs.:** Solicite o auxílio de um DBA para realizar os procedimentos via Banco de Dados, pois uma alteração em um campo que possui controle, faz-se necessário o recálculo do controle da tabela.  Recomendamos os testes em ambiente de homologação. |
