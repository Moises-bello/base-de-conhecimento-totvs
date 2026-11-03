---
content_hash: 3b275fc250f74e43efa0ea45a9adfd3199f88921164cb4d218258ff7a9c2fbd6
fetched_at: '2026-06-29T00:10:41.774824+00:00'
page_id: '546670617'
product: rm
source: tdn-rm
title: Novidades 12.1.29 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546670617
version: 21
---

### Aluguel

* Melhorias no cadastro de [contrato de administração](https://tdn.totvs.com/pages/viewpage.action?pageId=435105254):
  + A opção "Cobrança do Imposto sobre o Repasse do Contrato de Administração" define se os tributos decorrentes das transações financeiras deverão ser pagos pelo proprietário ou pela administradora.
  + No processo de [geração de movimento de administração](https://tdn.totvs.com/pages/viewpage.action?pageId=435105353),  quando o contrato de administração está definido para cobrança de impostos pelo proprietário, o movimento gerado para este contrato será gerado desagrupado, ou seja, um movimento para cada contrato de locação associado aos imóveis do contrato. Além disso, quando o contrato de administração está definido para cobrança de impostos pelo proprietário, os lançamentos que compõem o movimento passam a ser exibidos nos anexos de lançamento dos contratos de aluguel.
* Implementado o processo "[Gerar lançamento financeiro de previsão](https://tdn.totvs.com/pages/viewpage.action?pageId=544735159)", permitindo que os lançamentos dos contratos de aluguel sejam gerados quando o mesmo esteja em elaboração.
* Melhoria no processo de [geração de lançamentos futuros](https://tdn.totvs.com/pages/viewpage.action?pageId=544735159): Quando houver documentos do tipo de previsão associados ao parâmetro de "Utiliza lançamentos futuros como provisão" o sistema irá valer-se dos documentos cadastrados (A receber / A pagar) no parâmetro de integração financeira.
* Será possível efetivar [contratos de aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=520659174), [aditivos](https://tdn.totvs.com/pages/viewpage.action?pageId=435104996) e [escalonamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105312) que se encontrem na situação "Em aprovação".
* Criação do [anexo de documentos para Aluguel](https://tdn.totvs.com/pages/releaseview.action?pageId=549495253). Com este anexo será possível anexar um arquivo .pdf que poderá ser baixado ou visualizado no sistema.
* Disponibilizado o aditivo de [renegociação de dívidas](https://tdn.totvs.com/pages/releaseview.action?pageId=547865478) para contratos de aluguel.
* Melhorias no processo do Fechamento de Condomínio: Foram disponibilizadas as opções de inclusões de cobrança direta complementar e adiantamento de cobrança. Maiores detalhes [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=553349238) e [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=553349730).

### Venda

* Melhoria no renegociador do portal , usando a estrutura do aditivo existente. [Clique Aqui !](https://tdn.totvs.com/display/public/LRM/Aditivo+-+Renegociador+Portal)
* Alteração Global Cadastro de Venda - Eventos contábeis. [Clique Aqui !](https://tdn.totvs.com/pages/viewpage.action?pageId=549501260)
* Nova Revitalização - [Clique Aqui !](https://tdn.totvs.com/pages/viewpage.action?pageId=546260610)
* Diagnóstico do De/Para de Integração ( Ferramenta de Diagnóstico ) [Clique Aqui!](https://tdn.totvs.com/pages/viewpage.action?pageId=556868073)
* Vendedor Principal no Contrato . [Clique Aqui!](https://tdn.totvs.com/display/LRM/Vendedores)
* Processo para desfazer os aditivos de venda . [Clique Aqui!](https://tdn.totvs.com/display/public/LRM/Desfazer+Aditivo)
* Utilitário de backup e restore. [Clique Aqui!](https://tdn.totvs.com/pages/releaseview.action?pageId=553328444)

### **Portal do Cliente / Meu Imóvel**

* **Meu Imóvel**: Agora é possível acessar os [documentos de aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=515691276) no menu de documentos do aplicativo.
* **Meu Imóvel:** Disponibilizada a opção de renegociação para contratos de aluguel. [Clique Aqui!](https://tdn.totvs.com/pages/viewpage.action?pageId=518482641#MeuIm%C3%B3vel-Situa%C3%A7%C3%A3oFinanceira-3)RenegociarD%C3%ADvida)
* **Portal do Cliente**: Agora é possível acessar os [documentos de aluguel](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Documentos+-+Portal) no menu de documentos do Portal.

### **Integração Protheus**

* **Conversão EAI 2.0:**Disponibilizado o conversor para o
* **Configurador EAI 2.0:**Agora é possível realizar a configuração do
