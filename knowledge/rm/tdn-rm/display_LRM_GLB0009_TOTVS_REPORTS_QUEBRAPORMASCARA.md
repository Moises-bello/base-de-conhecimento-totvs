---
content_hash: aea03a3a7acf2285ac0ef8b422cab22f0938157116a0fd1225b2a5e7006c923d
fetched_at: '2026-06-29T00:06:19.956132+00:00'
page_id: '221545913'
product: rm
source: tdn-rm
title: GLB0009_TOTVS_REPORTS_QUEBRAPORMASCARA
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0009_TOTVS_REPORTS_QUEBRAPORMASCARA
version: 18
---

# QUEBRA POR MÁSCARA

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.9 |
| **Ocorrência:** | Totvs Reports |
| **Ambiente:** | Biblioteca RM |
| **Passo a passo:** | **Objetivo**:   ---   O objetivo dessa página é detalhar a funcionalidade “**quebra por máscara**” disponível no Totvs Reports.  Esse recurso faz com que os dados localizados em uma banda de detalhe sejam agrupados por determinadas posições de máscara.    **Como Configurar:**   ---     a) - No design do relatório, selecione a banda de "Cabeçalho de detalhe";        b) - Na janela de propriedades da banda selecione "Quebra por máscara";       falseDICA:   Para acessar as propriedades do componente de forma fácil, selecione-o e tecle F4.    c) - Será aberta uma janela para o usuário informar os dados da quebra. O usuário poderá adicionar ou remover uma ou mais quebras por máscara.         * ***Tabela***: Selecione a tabela do campo que será utilizado na quebra por máscara. Somente as tabelas inclusas no relatório serão listadas. * ***Coluna:*** Selecione a coluna que seus dados serão utilizados na quebra por máscara. Todas as colunas da tabela serão listadas.      * ***Controle:** S*erão listados todos os controles (Campos da Base) localizados na banda de "cabeçalho de detalhe".  Trata-se de uma informação opcional. Ela poderá ser útil em relatórios que precisem mostrar novo valor após a quebra.  Serão listados somente controles que possuem ligação com campos de tabelas serão listados.  * ***Quebra***: O usuário deverá informar interrogações "?" e/ou asterisco \*\*\* para definir a quebra. Exemplo:  Ex: Configuração da quebra:  \*\*\*?? [  ] Código da Seção = **001.05**  Uso de Interrogação ( ? ): Permite a quebra sempre que encontrar variação nos códigos. No exemplo acima, o valor "**05**" será recuperado pelas posições (  );  Uso de Asteriscos ( \* ): Simplesmente permite a classificação de dígitos tantos quantos forem os asteriscos utilizados. * ***Ordenação decrescente***: Caso esteja configurando uma ordenação, informe se ela será de forma decrescente ou crescente (padrão). Para ordem decrescente, marque (habilite) o campo. falseOBSERVAÇÃO: Ao clicar no botão "+Adicionar", as informações de ligação do controle serão validadas. Serão inclusos somente a "tabela" e o "campo" da ligação correspondente a "tabela" e o "campo" do agrupamento. Caso contrário, será exibido uma mensagem.  Impressão de relatórios:  **1) - No exemplo abaixo, não houve nenhum tipo de quebra:**  **2) - No exemplo abaixo, houve uma quebra pela campo Código da seção (não houve quebra por máscara).**  Para configurar uma quebra normal (sem quebra por máscara), basta usar a propriedade "Ordenação/Quebra" da banda de "cabeçalho de detalhe".   **3) - No exemplo abaixo, houve uma quebra por máscara (escopo de documento).**  O campo código da seção foi quebrado e agrupado pelas duas últimas posições. |
|  |  |
| **Observações:** |  |

divs
