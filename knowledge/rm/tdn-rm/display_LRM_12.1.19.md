---
content_hash: 48ffb16fb2b31097813c9caf14c54dd516212b5b918205f9dd9d3f94a281a7e5
fetched_at: '2026-06-29T00:09:23.222334+00:00'
page_id: '422546072'
product: rm
source: tdn-rm
title: 12.1.19
type: documentation
url: https://tdn.totvs.com/display/LRM/12.1.19
version: 7
---

* Alteração nas parametrizações do [Certificado Digital](http://tdn.totvs.com/display/LRM/Certificado+Digital) para emissão das Notas Fiscais Eletrônicas.
* A partir desta versão será utilizado o cadastro de Certificados Digitais e não será mais necessário informar o caminho do mesmo e sim seu ID no cadastro. Esta alteração visa melhorar a execução do processo em ambientes de múltiplas camadas.
* Alteração na tela dos [Outros Tributos do item do Lançamento Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422545658) para atender a geração dos registros R-2010 Retenção Contribuição Previdenciária - Tomadores de Serviços, R-2020 Retenção Contribuição Previdenciária - Prestadores de Serviços e R-2050 Comercialização da Produção por Produtor Rural PJ/Agroindústria da Reinf.
* Alteração no [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=422545996) apenas para o layout integrado com o TAF, para que as preferências do usuário sejam gravadas na tela de geração assim sendo desnecessário selecionar/digitar todos os parâmetros novamente.

* .
* Foi implementado o processo de [Cancelamento da NFS-e](http://tdn.totvs.com/display/LRM/Cancelar+NFS-e) e Movimento quando o município não disponibiliza integração eletrônica para o cancelamento da NFS-e.
* [Implementação do Município de Indaiatuba - SP - DESISS (txt)](http://tdn.totvs.com/pages/releaseview.action?pageId=64651845).
* DIME SC -Registro Tipo 26

2
incomplete
Criado um novo Subtipo "Crédito relativo Substituição Tributária", no Lançamentos de Outros Débito\Crédito, para geração do [Item 050 - Crédito de ICMS Retido por Substituição Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=422545651).

3
incomplete
FUNRURAL -   
  

* NFS-e Dourados - MS.

4
incomplete
Foi homologação a emissão da NFS-e de Dourados - MS com as operações de Autorização e Cancelamento da NFS-e

5
incomplete
Adequação da NFS-e de Aracaju ao layout único do TSS -  Foi modificado a regra de geração da TAG IEST para ser gerada nos casos em que a CFOP está configurada como Diferencial de Alíquota.  
 Com a nova regra a TAG IEST será gerada se a regra de ICMS da CFOP estiver configurada como "Substituto Tributário" no quadro "Situação da Retenção ICMS S.T." da aba "Dados ICMS S.T." E no cadastro da filial estiver vinculada uma IEST referente ao estado de destino da operação. Podendo o quadro "Operação Tributária" estar com qualquer opção selecionada, ou seja, este campo não interfere na geração da TAG.

* Criada a flag [Programa de Aquisição de Alimentos (PPA)](http://tdn.totvs.com/display/LRM/Dados+Fiscais).

* [Gerar registro C197 para IPI não Tributado no SPED Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422546128).

* A partir desta versão as guias de [INSS](http://tdn.totvs.com/pages/viewpage.action?pageId=422545658) também carregarão o valor do tributo constante nos itens do lançamento para a sua geração.
* [Alteração na geração do EFD Contribuições para o preenchimento do campo COD\_CTA dos reguistros:](http://tdn.totvs.com/display/LRM/Preenchimento+do+campo+COD_CTA+dos+registros)  
  Bloco A: A170  
   Bloco C: C170, C175, C381, C385, C396, C481, C485, C501, C505, C601, C605, C870, C880.  
   Bloco D: D100, D101, D105, D201, D205, D300, D350, D501, D505, D601, D605.  
   Bloco F: F100, F500, F510, F525, F550.  
   Bloco P: P100.  
   Bloco M: M400, M410, M800, M810.  
   Bloco 1: 1900.
