---
content_hash: 110b941d81bb522fd7bbd82bc4f6ac017bc13085c9e0a991d35d157407c7836b
fetched_at: '2026-06-29T00:09:26.772606+00:00'
page_id: '423938418'
product: rm
source: tdn-rm
title: Aumentar Máscara do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938418
version: 5
---

O aumento da máscara do patrimônio deverá ocorrer quando o último nível, da máscara atual, não comportar a quantidade de patrimônios existentes. Na tela de processo serão apresentados os campos "Máscara atual" e "Máscara nova". O primeiro deverá ser preenchido automaticamente e não poderá ser a modificado. O segundo deverá receber a nova máscara, que passará pelas seguintes validações:

* O preenchimento da máscara nova será obrigatório.
* A nova máscara deverá ser diferente da atual.
* Não poderão ser adicionados novos níveis na nova máscara.
* O último nível deverá ser maior na nova máscara, porém o tamanho dos níveis anteriores não poderá ser modificado.

Exemplo: Caso a máscara atual seja ##.##.### a nova máscara não poderá ser alterada para #####.##.##, pois o tamanho do primeiro nível foi alterado. Já a máscara ##.##.##### é valida, pois o tamanho dos dois primeiros níveis não foi alterado e o último nível ficou maior.  
Passando por estas validações a máscara irá aumentar, provocando a alteração dos códigos dos patrimônios. Em função destas mudanças os registros existentes na tabela IPATRIMONIO serão alterados para contemplarem os novos códigos. Vale ressaltar que até mesmo os patrimônios que sofreram uma baixa total ou que foram baixados em período anterior terão seus códigos alterados para atender a nova máscara. Por fim será gerado um log informando o que foi realizado durante a execução do processo.

Caso o ambiente esteja configurado para [N Camadas](https://tdn.totvs.com.br/display/LRM/Ambiente+3+Camadas) é possível programar a execução deste processo para um horário posterior.
