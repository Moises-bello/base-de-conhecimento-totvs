---
content_hash: 232f0e3da87e3bf75b81fb4a52e9d14d9ab0493a1d2e0f3aa91a0600a9945441
fetched_at: '2026-06-29T00:09:16.090636+00:00'
page_id: '421385455'
product: rm
source: tdn-rm
title: Exportação Off-line de TOTVS Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385455
version: 2
---

---

Foi feita a migração da funcionalidade em Delphi: Geração de Movimentos para Folha de Pagamento. A funcionalidade de importação dos novos layouts será feira no Gerador de Saída.  
 **Geração de Saída**  
 Esta opção irá gerar as apropriações de funcionários do projeto para serem exportados para o Folha de Pagamento.  
 Poderá ser utilizado arquivo de movimento e substituição.

* **Seleção de Layout**
  + Layout: Selecionar o arquivo de layout para ser gerado.
  + Diretório de Destino: Informe onde o arquivo gerado será gravado.
* **Parâmetros da Geração**
  + Data Inicial: Informe a data de início das apropriações a serem exportadas.
  + Data Final: Informe a data final das apropriações a serem exportadas.
  + Data do Pagamento: Informe a data do pagamento dos eventos (provento) dos movimentos. Esse campo só ficará ativo para a geração do arquivo de movimentos.
  + Usar evento indicado na apropriação: Marque essa opção se desejar que as apropriações sejam exportadas com o evento definido no seu cadastro. Esse campo só ficará ativo para a geração do arquivo de movimentos.
  + Evento**:** Informe o evento (proventos) dos movimentos que não possuem evento na apropriação ou para os quais será gerado o arquivo. Caso a opção 'Usar evento indicado na apropriação' esteja marcada o evento informado no momento de gerar o arquivo será considerado somente para as apropriações que não possuem um evento em seu próprio cadastro. Esse campo só ficará ativo para a geração do arquivo de movimentos.

**Observação:**   
 O arquivo de substituição de funcionários é importado através do menu Configurações| Importações | Importações de Dados do RM Labore. Na pasta Parâmetros, marque a opção 'Funcionários', na pasta Funcionários II marque a opção 'Controle de Substituição'.  
 **Atenção:**   
 Caso o evento que será enviado ao Folha de Pagamento esteja com o campo 'Valor/Hora/Dia/Ref' marcado para 'Valor' na visão de cadastro de eventos do Folha de Pagamento, o sistema irá exportar a Quantidade \* Preço Unitário apropriado no Construção e Projetos, considerando o parâmetro de casas decimais monetárias parametrizada no Construção e Projetos. Qualquer outra opção do campo 'Valor/Hora/Dia/Ref' que esteja marcada, será exportado o número de horas apropriadas no Construção e Projetos.

|  |  |
| --- | --- |
|  | Veja Também |

---

Gerador de Saída
