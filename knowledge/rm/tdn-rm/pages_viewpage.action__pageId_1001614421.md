---
content_hash: dd1e00983455bfd384e9eb9c6ff1ab2be5683ce4c99be45e67a7d192d427acca
fetched_at: '2026-06-29T00:05:45.014704+00:00'
page_id: '1001614421'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Situação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1001614421
version: 8
---

Tela de **configuração de parâmetros** para emissão de boletos na Situação Financeira.

### Parâmetros de Configuração do Portal do Cliente

* **Exibir todo o plano de financiamento:** Se a opção estiver desmarcada o Portal do Cliente irá exibir as parcelas vencidas e a parcela que vence no mês atual. Se a opção estiver marcada serão exibidas todas as parcelas, incluindo as vincendas.
* **Permite antecipação de pagamento:**Este parâmetro permite a incorporadora indicar se o Portal TIN deve ou não disponibilizar parcelas financeiras com vencimento futuro para antecipação do pagamento. Para o correto funcionamento do recurso de Antecipação de Pagamento, o recurso de reajuste online do financeiro deve estar ativado para cálculo de valores contratuais(Juros e CM), caso contrário não haverá atualização dos valores contratuais.
  + **Pode antecipar, mesmo com parcela atrasada:** Marque esta opção para permitir que o cliente possa antecipar o pagamento das parcelas vincenda (a vencer), mesmo que ele tenha parcelas vencidas, em aberto.
  + **Ordem de antecipação de pagamento:** Utilize essa opção para definir em qual ordem o cliente pode selecionar as parcelas para a antecipação, sendo:
    - *Qualquer parcela*: o cliente pode selecionar qualquer parcela da lista para antecipar.
    - *Da primeira para a última*: o cliente só pode antecipar as parcelas em ordem crescente de vencimento, em relação à data de acesso ao PDC.
* **Limitar vencimento do boleto até o último dia do mês atual:** Utilize esse opção para limitar o vencimento do boleto para até o último dia do mês de acesso ao PDC.
* **Número máximo de dias para vencimento do boleto:** Defina o número máximo de dias, em relação à data de acesso ao PDC, para que o cliente possa definir a data de vencimento do boleto. Este parâmetro respeita a parametrização  acima, sendo que o sistema não aceita números  negativos.

---

* **Permite gerar novo boleto parcela vencida e do mês:** Nem todas as empresas permitem que sejam gerados novos títulos para parcelas já vencidas sendo necessário a parametrização para que cada cliente estabeleça seus próprios critérios.
* **Opções de pagamento para as parcelas:**Este parâmetro define se novos boletos ou a antecipação de boleto será feita pelo processo de registro online ou pelo processo de gerar boletos não registrados. Abaixo temos uma explicação de cada item:
  + **Registro Online**: A geração do boleto é feita pela entidade bancária. Ao selecionar essa opção, o cliente **habilita a etapa de configuração dos dados bancários**, que devem ser informados para viabilizar a integração com o banco emissor.
  + **Pix TPD:** O Pix para pagamento desse boleto é gerado diretamente na entidade bancária cadastrada para o cliente, sem a intermediação de nenhuma outra entidade bancária.
  + **Registro Online / Pix TPD**: São geradas as duas opções de pagamento acima, cabendo ao cliente escolher a que melhor lhe atende.  
    Assim como na opção *Registro Online*, **essa seleção também habilita a etapa de dados bancários**, necessária para o correto funcionamento das duas modalidades de pagamento.
  + **Boleto Híbrido**: Geração do boleto com código de barras e o QrCode do Pix, ou seja as duas modalidades de pagamento em um único documento. Para mais informações e instruções de configuração, acesse [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1).

* **Exibir Valores Sumarizados do Contrato:** Permite exibir ou não os campos de "Valor Total Financiado Atualizado", "Saldo Devedor" e "Valor Total Pago" da visão de Situação Financeira
* **Limitar o acesso do Comprador Principal desativado:** Essa opção permite limitar o acesso do antigo Comprador Principal, para que ele veja somente as parcelas e os boletos que estão atribuídos a ele e não mais os de todo o contrato.
