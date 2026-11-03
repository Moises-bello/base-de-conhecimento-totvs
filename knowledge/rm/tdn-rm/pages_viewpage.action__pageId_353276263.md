---
content_hash: 165ee549fce4cea849875cc227334ff3e2afcc2bef3ad672b7c19c51059a9fc3
fetched_at: '2026-06-29T00:08:57.159383+00:00'
page_id: '353276263'
product: rm
source: tdn-rm
title: RMPAT000010_Aumentar Máscara do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353276263
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Aumentar Máscara do Patrimônio |
| **Ambiente:** |  |
| **Passo a passo:** | O aumento da máscara do patrimônio deverá ocorrer quando o último nível, da máscara atual, não comportar a quantidade de patrimônios existentes.   Na tela de processos serão apresentados os campos “Máscara atual” e “Máscara nova”. O primeiro deverá ser preenchido automaticamente e não poderá ser a modificado. O segundo deverá receber a nova máscara, que passará pelas seguintes validações:   * O preenchimento da máscara nova será obrigatório. * A nova máscara deverá ser diferente da atual. * Não poderão ser adicionados novos níveis na nova máscara. * O último nível deverá ser maior na nova máscara, porém o tamanho dos níveis anteriores não poderá ser modificado.   **Exemplo:** Caso a máscara atual seja ##.##.### a nova máscara não poderá ser alterada para #####.##.##, pois o tamanho do primeiro nível foi alterado. Já a máscara ##.##.##### é válida, pois o tamanho dos dois primeiros níveis não foi alterado e o último nível ficou maior.  Passando por estas validações a máscara irá aumentar, provocando a alteração dos códigos dos patrimônios. Em função destas mudanças os registros existentes na tabela IPATRIMONIO serão alterados para contemplarem os novos códigos. Vale ressaltar que até mesmo os patrimônios que sofreram uma baixa total ou que foram baixados em período anterior terão seus códigos alterados para atender a nova máscara.    **Realizando o Aumento na Máscara do Patrimônio:** Acessar: Utilitários | Aumentar Máscara do Patrimônio.      Preencha o campo da Máscara Nova, aumentando a quantidade de caracteres do último campo do código do patrimônio:        Após o preenchimento da Máscara Nova, execute o processo.        Por fim será gerado um log informando o que foi realizado durante a execução do processo.        Cadastro de patrimônio antes da execução do processo:        Cadastro de patrimônio depois da execução do processo: |
| **Observações:** |  |
