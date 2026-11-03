---
content_hash: 2bece85ed05577fbd6760f1e0cf4e381aad50464dcd9bfd0bf32393db0f579e3
fetched_at: '2026-06-29T00:10:03.142266+00:00'
page_id: '452719025'
product: rm
source: tdn-rm
title: Férias Coletivas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719025
version: 9
---

Nesta etapa será definido como será tratado o período aquisitivo nas férias coletivas.  
   
**Campos e Parâmetros**

Considera data retorno para início período aquisitivo quando < 1 ano  
Quando houver cadastro de férias coletivas o novo período aquisitivo será iniciado quando houver o término do período concessivo de férias.  
**Exemplo:** Data de admissão 01/09/2023   
Data das férias coletivas 21/12/2023 a 31/12/2023 - 10 dias  
Próximo período aquisitivo = 01/01/2024 a 31/12/2024

**Observação:** Caso o funcionário não tenha dias de direito de férias quando for cadastrado pelo processo Coletivas/Globais será apresentada a mensagem: "A Licença Remunerada deverá ser informada manualmente no Histórico de Afastamentos.".   
**Exemplo:**  
Parâmetro desmarcado   
Férias coletivas 26/12/2023 a 05/01/2024 - 11 dias  
Admissão em 12/12 contando os dias até 25/12, ou seja um dia antes do inicio das férias = 14 dias então apresenta mensagem  
Admissão em 11/12 contando os dias até 25/12, ou seja um dia antes do inicio das férias = 15 dias então cadastra férias coletivas e não apresenta mensagem

Parâmetro marcado   
Férias coletivas 26/12/2023 a 05/01/2024 - 11 dias  
Quando a admissão é dentro do mês de inicio das férias coletivas, dependendo da data o funcionário tem direito a 2,5 dias correspondente a 1 avo de férias. Nesse caso as férias iniciariam em 26/12 e terminariam em 28/12 contando o restante como licença remunerada.   
Portanto, a contagem para apresentar a mensagem seria da data de admissão até 28/12 que seria o final das férias coletivas informado no processo de cadastramento.  
Admissão em 15/12 contando os dias até 28/12 = 14 dias apresenta mensagem  
Admissão em 14/12 contando os dias até 28/12 = 15 dias Cadastra e não apresenta mensagem

DICA

Veja também parâmetro "Paga licença para quem tem menos de 1 ano" no cadastro de Sindicatos TDN [Sindicatos](https://tdn.totvs.com.br/display/LRM/Sindicatos)

IMPORTANTE:

Quando houver o cenário que o funcionário tiver por exemplo 27,5 dias de direito a férias e com isso menos de um ano na empresa.

A empresa concede 20 dias de férias coletivas, então restam 7,5 dias para conceder de férias para esse funcionário que são ainda do período aquisitivo inicial, portanto será aberto novo período aquisitivo sem fechar o anterior. Ficando os dois períodos em aberto.

   
 Mantém período aquisitivo quando < 1 ano

O período aquisitivo do funcionário não será alterado quando este parâmetro estiver marcado e o funcionário tiver menos de um ano de admissão.

Parâmetro Marcado

Lançamento de férias coletivas para funcionário com menos de 1 ano de admissão:

Cadastro das férias após o lançamento:

Importante:

Como será considerado para manter o período aquisitivo do funcionário que tem menos que 1 ano de admissão, então foram antecipados dias de direito de férias.

Veja que não foram cadastrados dias de licença remunerada e férias a marcar ficou negativo, considerando os dias que ainda serão adquiridos dentro do período aquisitivo.

Parâmetro Desmarcado

Lançamento de férias coletivas para funcionário com menos de 1 ano de admissão:

Cadastro das férias após o lançamento:

Importante:

Como não será considerado o período aquisitivo do funcionário que tem menos que 1 ano de admissão, então foram cadastrados os dias de direito de férias.

Veja que foram cadastrados dias de licença remunerada e férias a marcar ficou zerado.

O novo período aquisitivo será criado de acordo com os parâmetros do sistema.

 Evento para pagamento de licença remunerada  
   
   
 Motivo de afastamento por licença remunerada  
 

<< Retornar para **Férias**
