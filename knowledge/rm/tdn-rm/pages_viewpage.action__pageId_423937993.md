---
content_hash: 1786db0c46915a30af19a1dc50a186d0eaeb53e60e5d8e09bb4a8112f055593b
fetched_at: '2026-06-29T00:09:24.679738+00:00'
page_id: '423937993'
product: rm
source: tdn-rm
title: Relatório de Depreciação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937993
version: 5
---

O relatório de depreciação permite conferir individualmente os valores de depreciação calculados para cada um dos patrimônios. Através deste menu é possível emitir informações agrupadas por grupo de patrimônio, conta contábil, centro de custo ou filial.

**Regras para emissão do relatório**

Como pré-requisito para composição deste relatório, deverão ser importados no gerador de relatórios os arquivos abaixo:  
PATREL0014- Relatório de Depreciação

PATREL0015 - Relatório de Depreciação por Centro de Custo

PATREL0016 - Relatório de Depreciação por C. Custo (Sintético c Contas)

PATREL0017 - Relatório de Depreciação por C. Custo (Sintético)

PATREL0018 - Relatório de Depreciação por Filial

PATREL0019 - Relatório de Depreciação por Filial (Sintético c Contas)

PATREL0020 - Relatório de Depreciação por Filial (Sintético)

PATREL0021- Relatório de Depreciação (Sintético)

Esses arquivos funcionam como layout para apresentação das informações, e estarão disponíveis no diretório de instalação totvs\CorporeRM\ObjetosGerenciais\Relatórios

**Emissão do relatório de depreciação**

Inicialmente devem ser informados os meses e anos, respectivamente, iniciais e finais desejados para apuração (período de apuração), quais patrimônios serão envolvidos (os ativos e/ou inativos) e o cenário de cálculo correspondente a estes patrimônios.

Caso seja necessário, pode-se selecionar uma ou mais filiais. Desta forma somente as informações dos patrimônios existentes nas filiais selecionadas serão exibidas. Caso não seja selecionada filial, o sistema exibirá informações de todas as filiais, conforme o restante da parametrização.

O usuário poderá selecionar o status das depreciações que deseja exibir:

Não contabilizadas: serão exibidas com o status contabilização "N"

Não Integrada: Serão exibidas com o status contabilização "CN"

Integrada: Serão exibidas com o status contabilização "CI"

Contabilizada: Serão exibidas com o status contabilização "C"  
   
Caso não seja selecionado o status de contabilização, o sistema exibirá informações de todas as depreciações, conforme o restante da parametrização.  
A maneira como as informações serão pesquisadas é extremamente importante para que os dados mantenham sua integridade. Sendo assim, ao avançar etapa o usuário poderá filtrar por um ou mais grupos de patrimônio. Caso não seja selecionado grupo de patrimônio, o sistema exibirá informações de todos os grupos.

Para que o Patrimônio seja emitido no relatório, o Grupo de Patrimônios deve possuir no  contas com Classificação Contábil de "*Depreciação*" e, caso deseje exibir a realização das avaliações patrimoniais, com a Classificação Contábil "*Realização da Avaliação*".

Antes de emitir o relatório é necessário selecionar o layout do relatório de depreciação que deseja.
