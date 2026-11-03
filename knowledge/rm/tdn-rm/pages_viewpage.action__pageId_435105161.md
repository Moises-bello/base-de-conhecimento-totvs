---
content_hash: bdbdb551d74237797fa62362bcfe89bcdf789febd6b0b0ca8fcca8f4114ac5bd
fetched_at: '2026-06-29T00:09:48.466246+00:00'
page_id: '435105161'
product: rm
source: tdn-rm
title: Relatórios - DIMOB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105161
version: 27
---

---

## 📄DIMOB – Declaração de Informações sobre Atividades Imobiliárias

**A DIMOB (Declaração de Informações sobre Atividades Imobiliárias)** é uma **entrega obrigatória à Receita Federal do Brasil**, utilizada para **cruzamento fiscal dos contribuintes**.  
Essa declaração informa os detalhes das **transações imobiliárias realizadas**, destacando principalmente:

* Identificação dos contratantes
* Identificação do imóvel
* Data da operação
* Valor da operação
* Comissão cobrada

Excetuam-se dessa obrigatoriedade as **microempresas e empresas de pequeno porte** enquadradas no **regime especial unificado de arrecadação de tributos e contribuições**.

No **TOTVS Incorporação**, a geração da DIMOB é realizada para:

* **Módulo de Vendas** (Contratos | Vendas)
* **Módulo de Aluguéis** (Aluguéis | Contrato de Locação)

⚠️ **Atenção:**  
Caso os valores das operações informadas não estejam coincidentes, a declaração poderá ficar **retida em malha fina**, havendo a possibilidade de **aplicação de multa e juros** sobre a diferença entre o valor declarado pelo contribuinte e o valor informado pelas empresas na DIMOB.  
As empresas também podem ser multadas caso as informações prestadas **divirjam do que foi efetivamente praticado**.

---

## 🏢Quem deve entregar a DIMOB

Devem entregar a DIMOB:

* Pessoas jurídicas e equiparadas que **comercializaram imóveis** que construíram, lotearam ou incorporaram para esse fim;
* Pessoas jurídicas que **intermediaram aquisição, alienação ou aluguel de imóveis**, ou realizaram **sublocação**;
* Pessoas jurídicas constituídas para **construção, administração, locação ou alienação** de patrimônio próprio, de seus condôminos ou sócios.

📅 A DIMOB é uma **declaração anual**, com prazo de entrega até o **último dia útil de fevereiro**.  
O envio fora do prazo implica **aplicação de multa**, portanto é importante atenção à data de entrega.

---

## **⚙️**Geração da DIMOB no TOTVS Incorporação

No **TOTVS Incorporação**, a geração da DIMOB está disponível em: **Relatórios | DIMOB**

Durante o processo, estão disponíveis as seguintes configurações:

* **Coligadas:**  
  Ao selecionar o processo da DIMOB, será exibida uma tela para selecionar a(s) coligada(s);
* **Caminho:**  
  Informe o local onde o(s) arquivo(s) gerados serão salvos;
* **Opções de Agrupamento:**

  + Sem nenhuma opção marcada: será gerado **um único arquivo**, contendo os dados de todos os empreendimentos;
  + **Gerar um arquivo por empreendimento:** cria um arquivo para cada empreendimento;
  + **Gerar um arquivo por parceiro de acordo com o repasse:** cria um arquivo para cada repasse de cada empreendimento.

    - *ℹ️ Considera-se **parceiro(a)** a empresa que possui percentual de participação no recebimento dos valores do empreendimento.   
      Para cadastrar um repasse, acesse: **Menu: Venda** **| Manutenção de Empreendimentos | Empreendimento | Anexos | Dados de Repasse | [Incluir]***
* **Ano Calendário:** Informe o ano de referência das atividades imobiliárias;
* **CPF do responsável:** CPF do responsável pela geração do arquivo;
* **Declaração Retificadora:** Utilizada quando houver incorreção ou omissão de informações;
* **Situação Especial:** Utilizada em casos de extinção, fusão, incorporação ou cisão total da pessoa jurídica.
* **Opções de Agrupamento Locação:** Quando as partes do contrato forem as mesmas;
* **Identificador do Contrato Locação:** Poderá ser selecionadoNúmero do contrato ou Código que será gerado no arquivo.
* **Valor Total da Operação:** Pode ser:

  + Valor de Venda
  + Valor do Financiamento
  + Valor do Item da Venda

---

## 🔁Comportamento da DIMOB conforme modelo de repasse

O comportamento da DIMOB depende do **modelo de repasse definido no contrato de administração**:

* **Repasse do tipo Garantido:**  
  Encargos moratórios (juros e multa) e descontos são considerados da **administradora**, não sendo repassados ao(s) proprietário(s);
* **Repasse do tipo Condicional:**  
  Sempre serão considerados os valores dos respectivos campos para cálculo dos encargos moratórios (juros e multa) e descontos na DIMOB.

---

* Ao final do processo, é gerado um **arquivo TXT**, que deverá ser **importado no programa da DIMOB**, disponibilizado pela Receita Federal.

false

## 🔎 Observações:

📌 **Aluguel**  
No Aluguel, a DIMOB é gerada apenas quando houver **baixas no período selecionado**.  
Caso haja necessidade de utilizar fórmulas para compor o valor do arquivo, acesse:  **➡️ *[Contrato de Locação - Dados Gerais](https://tdn.totvs.com.br/pages/viewpage.action?pageId=520659174)***

📌 **Venda**  
Na Venda, a DIMOB é gerada no ano em que foi cadastrada ou no ano em que ocorrer a troca de comprador, **independentemente da geração de contrato**.

📌 **Composição do Valor da Operação**  
Ainda na Venda, o valor total da operação gerado no DIMOB será composto pela **soma dos componentes do plano**, considerando o parâmetro **“Desconsiderar valor na exportação para SPED / DIMOB”** de cada componente.  
Para mais detalhes sobre o funcionamento desse parâmetro, **➡️ [acesse aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154#:~:text=Reserva%3A%20Utilizado%20para%20identificar%20se%20o%20empreendimento%20entra%20para%20a%20lista%20de%20empreendimentos%20processados%20pelo%20DIMOB.).**

📌 **Repasse por Unidade ou Subunidade**  
Caso exista algum percentual de repasse cadastrado (**Unidade ou Subunidade**), o valor calculado para o campo **Valor da Operação** considerará apenas a **parte da incorporadora**.

📌 **Exclusão de Empreendimentos**  
Para desconsiderar o envio de todos os contratos de um determinado empreendimento para o DIMOB, selecione o identificador **“Reserva”**.  
Para mais informações, acesse aqui.

📌 **Valor Pago no Ano**  
Os valores pagos que compõem o campo da DIMOB **“Valor Pago no Ano”** considerarão as datas de entrada e saída do plano de financiamento registradas no anexo do respectivo comprador da venda.

---

## ⚙️Parâmetro: Gerar log do cálculo da ficha de locação (tipo R2)

📍 **Caminho:** Gestão de Imóveis > Aluguel > Contrato de Locação > Gerar log do cálculo da ficha de locação (tipo R2)

## ❓ Para que serve esse parâmetro?

Este parâmetro define se o sistema deve gerar ou não um log detalhado do cálculo realizado na ficha de locação (processo conhecido como DIMOB, tipo R2).

O log é útil para auditar, conferir e validar os valores calculados  como valor bruto, comissão, impostos e itens de cobrança de cada contrato. Porém, em alguns clientes o log pode ficar muito grande, tornando o processo de geração mais demorado. Por isso, a geração desse log passou a ser opcional.

##### Comportamento do sistema

* Parâmetro desmarcado (padrão):  
  O sistema não gera o log de cálculo da ficha de locação.  
  Essa é a configuração recomendada para o uso normal, garantindo maior velocidade na geração da DIMOB.
* Parâmetro marcado:  
  O sistema passa a gerar o log detalhado.  
  Use esta opção apenas quando for necessário validar ou investigar os valores calculados no processo de locação.

##### Exemplo de uso

1. O usuário acessa o caminho:  
   Gestão de Imóveis > Aluguel > Contrato de Locação
2. Habilita o parâmetro “Gerar log do cálculo da ficha de locação (tipo R2)”.
3. Gera a DIMOB novamente.
4. O sistema exibe o *log detalhado* com as informações de cálculo por contrato, item de cobrança, valor bruto, comissão e imposto.

Caso o componente gerador da parcela estiver definido para desconsiderar o valor, então todos os demais componentes que compõem o valor desta parcela também serão desconsiderados independente da sua configuração.

**Exemplo**: Parcela é composta pelo componente Mensal, CM e Juros. O componente Mensal foi configurado para ser desconsiderado no valor final. Portanto o valor do componente Mensal, do CM e do Juros serão desconsiderados.

No mesmo exemplo acima, caso o usuário tenha definido que somente o componente CM seja desconsiderado, então o DIMOB irá gerar o valor composto pelo componente Mensal e Juros.

**Execução do processo de DIMOB via wsProcess**

Para que na execução do DIMOB via wsProcess os arquivos sejam gerados na pasta de destino,  é necessário que esta pasta se localize no próprio servidor que irá executar o processo além de colocar no XML de parâmetros do processo o valor do campo **ServerFolder** igual a **true.**

**Maiores informações sobre o DIMOB nos sites abaixo:**

* [DIMOB - Receita Federal](http://idg.receita.fazenda.gov.br/acesso-rapido/legislacao/legislacao-por-assunto/dimob)
* [Perguntas e Respostas sobre DIMOB - Receita Federal](http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/dimob-declaracao-de-informacoes-s-atividades-imobiliarias/perguntas-e-respostas)
