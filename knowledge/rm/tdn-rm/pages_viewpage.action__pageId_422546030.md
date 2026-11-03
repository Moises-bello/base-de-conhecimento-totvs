---
content_hash: a40e78097e19f98e3f2325e58f75c54e55e3c68de127c3c04eaa7e13623e9bd6
fetched_at: '2026-06-29T00:09:22.796143+00:00'
page_id: '422546030'
product: rm
source: tdn-rm
title: Alterar Modalidade de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546030
version: 7
---

De acordo com o manual de integração do contribuinte, as legislações específicas de cada Unidade da Federação e os vários [Ajustes SINIEF](https://www.confaz.fazenda.gov.br/legislacao/ajustes) as várias modalidades de emissão da NF-e são detalhadas:   
 Em condições normais o contribuinte emite a NF-e para sua SEFAZ do origem. Em caso de falha no processo de autorização da NF-e ou no ambiente  o contribuinte poderá alterar livremente a modalidade de operação que está utilizando e escolher a que for mais conveniente. Atualmente existem seis tipos de modalidade de emissão conforme descrito a seguir:

**Normal:** O processo de emissão normal é a situação desejada e mais adequada para o emissor, pois é a situação em que todos os recursos necessários para a emissão da NF-e estão operacionais e a autorização de uso é concedida normalmente pela SEFAZ. Nesta situação a emissão é a realizada normalmente com a impressão do DANFE em papel comum, após o recebimento da autorização de uso.

**Contingência OffLine:** Também conhecida como Contingência em Formulário de Segurança - FS", Sendo identificada a existência de qualquer incidente que prejudique ou impossibilite a transmissão das NF-e e/ou obtenção da autorização de uso da SEFAZ, a empresa poderá adotar essa Contingência. Nesta situação a emissão das NF-e é realizada normalmente com a impressão do DANFE em formulário de segurança. Sanado o problema que impedia a transmissão da NF-e esta deve ser transmitida para a SEFAZ em modo Normal.

**EPEC:** Uma das contingências previstas no modelo do sistema da NF-e é a possibilidade de autorização de uma Declaração Prévia de Emissão em Contingência (DPEC), contendo dados reduzidos da NF-e. A autorização da DPEC permite a emissão do DANFE em papel comum, considerando-se emitida a NF-e a partir do momento da impressão deste DANFE, sob condição de posterior transmissão da NF-e para a SEFAZ de origem do contribuinte.

**Contingência Offline FS-DA:** Sendo identificada a existência de qualquer incidente que prejudique ou impossibilite a transmissão das NF-e e/ou obtenção da autorização de uso da SEFAZ, a empesa poderá adotar este tipo de contingência. Nesta situação a emissão das NF-e é realizada normalmente com a impressão do DANFE em Formulário de Segurança para impressão de Documento Auxiliar de Documento Fiscal - FS-DA e substitui a contingência com o uso do formulário de segurança.

**SVC - AN:** O ambiente de autorização SVC, SEFAZ Virtual de Contingência, poderá assumir a recepção e autorização de uma outra unidade da federação quando solicitado pela SEFAZ de origem. Nesta situação a emissão das NF-e é realizada normalmente com a impressão do DANFE em papel comum, após o recebimento da autorização de uso da NF-e.

**SCV - RS:** O ambiente de autoriza da SVC, SEFAZ Virtual de Contingência, poderá assumir a recepção e autorização das NF-e de uma outra unidade da federação, quando solicitado pela SEFAZ de origem. Nesta situação a emissão da NF-e é realizada normalmente com a impressão do DANFE em papel comum, após o recebimento da autorização de uso da NF-e.  
 A mudança da modalidade de emissão é  feita através da visão das NF-e através do botão Processos | Alterar Modalidade de Operação.  Os parâmetros deste processo são a Filial, a Modalidade e o Motivo. Para todas as modalidades, com exceção da Normal, o campo Motivo é obrigatório.   
 Para a mudança de modalidade, se a integração do processo da NF-e é feita pelo TSS, o mesmo deve estar em execução.
