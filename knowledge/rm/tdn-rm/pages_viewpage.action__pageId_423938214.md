---
content_hash: 832141d90b82a96bd273f536fd4fafbeabc3b616cd631d66de3915f5b5f20da2
fetched_at: '2026-06-29T00:09:25.963271+00:00'
page_id: '423938214'
product: rm
source: tdn-rm
title: Assistente de Cópia por Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938214
version: 5
---

O processo de Cópia por Referência é utilizado para a utilização dos dados de um movimento 'origem', para a geração de um movimento 'destino' com as mesmas informações, evitando o retrabalho na digitação, além de efetuar o vínculo entre os movimentos quando utilizados determinados Motivos de Referência.  
Um exemplo sobre este vínculo a ser criado pela Cópia por Referência é no processo de Devolução de uma Nota Fiscal de Compras.  
Quando este documento de Nota Fiscal é devolvido, é gerado um documento pela empresa que está devolvendo esta Nota de Compras.   
Como esta devolução deve ser de materiais/serviços que foram discriminados na Nota de Compras, ao efetuar a Cópia por Referência, o sistema vai 'associar' o documento de devolução com o documento de compras, para manter a informação no movimento de compras sobre quais foram os materiais/serviços devolvidos. Deste modo, evita-se que sejam 'devolvidos' materiais ou serviços que não foram adquiridos pela empresa, além de evitar que a quantidade de devolução possa ser maior que a quantidade comprada.

**Parametrização**

Para a utilização do processo de Cópia por Referência, o tipo de movimento deve ser devidamente parametrizado, acessando-se a etapa 'Mov – Outros Dados', marcando a opção 'Usar Cópia de Movimentos por referência' e selecionando qual o Motivo de Referência a ser utilizado, dentre os disponíveis no sistema.  
Após a parametrização, ao ser apresentada a visão de movimentos deste tipo de movimento parametrizado, o menu Movimentos apresentará a opção 'Gerar Mov. por Referência' que, ao ser selecionado, apresentará um Assistente para conduzir à cópia.  
No Assistente, após a tela de boas vindas, deverão ser incluídos os movimentos a serem copiados.   
Neste momento, deverá ser clicado no ícone de 'Incluir', no canto superior esquerdo da tela.   
Ao clicar, será aberta uma tela onde deverão ser feitos os filtros desejados para a apresentação dos movimentos que se deseja copiar.   
Um exemplo pode ser efetuar um filtro pelo Tipo de Movimento e a Data de Emissão do Movimento, que podem ser utilizadas como parâmetros para que, todas as vezes que for executado este Assistente, este filtro receba os parâmetros do Tipo de Movimento e Data de Emissão, executando sempre da mesma forma, independente da parametrização do tipo de movimento a ser gerado.   
No caso de seleção de mais de um movimento será carregado os dados do 1º selecionado.   
Os campos pertencentes ao movimento selecionado para cópia e que não fazem parte da parametrização do movimento serão ignorados na cópia.   
Além disso, campos pertinentes à numeração e natureza de operação não serão copiados.

***Observações***:

* Na parte inferior direita do Assistente, é sempre disponibilizado, para consulta, qual o Motivo de Referência parametrizado no Tipo de Movimento, podendo ser consultado sobre quais as informações do seu cadastro, bastando clicar no link. Ao avançar para a próxima etapa do Assistente, serão apresentados os Itens dos movimentos selecionados na etapa anterior. Deverão ser selecionados os itens de movimentos que se deseja copiar. Após esta seleção, deverá ser avançada para a próxima etapa, finalizando o Assistente. Após a finalização do Assistente, será aberta a tela do Movimento a ser gerado, com os Itens selecionados dentro do Assistente, para a informação dos demais dados do documento.
* Nos movimentos de Devolução por cópia por referência, é possível incluir movimentos com o Cliente / Fornecedor do movimento de origem. No caso da geração de lançamentos financeiros pela movimentação, o tipo de documento deverá ser classificado como devolução para que não seja consistido o tipo de Cliente / Fornecedor.
* No caso de exclusão de movimentos que possuam movimentos devolvidos, o movimento de devolução deve ser excluído antes do movimento de origem.
* O Cliente/Fornecedor utilizado neste tipo de movimento deverá ser do tipo "Ambos", para que o sistema permita criar lançamentos financeiros tanto 'A Pagar' quanto 'A Receber'.
* Ao incluir um movimento de devolução de compras ou de vendas, pelo processo de cópia por referência, o sistema apresentará a Condição de Pagamento que foi informada no movimento de Nota Fiscal emitente, não considerando os tipos de planos da Condição de Pagamento.

Informações Adicionais

[Devolução de Compras de Mercadorias](http://tdn.totvs.com/pages/viewpage.action?pageId=233746740)

[Devolução de Vendas de Mercadorias](http://tdn.totvs.com/pages/viewpage.action?pageId=4813138)

[Reporta Insumos para Ordem de Serviço do módulo Manutenção de Ativos linha Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=583768340)
