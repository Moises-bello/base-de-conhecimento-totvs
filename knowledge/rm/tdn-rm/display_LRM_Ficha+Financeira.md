---
content_hash: 9cfb07cd5f2699cfc4f9f2858201b1b6c087c68c0627b2eb0d3e1834deb4249a
fetched_at: '2026-06-29T00:10:08.606844+00:00'
page_id: '452719545'
product: rm
source: tdn-rm
title: Ficha Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/Ficha+Financeira
version: 6
---

Nesta etapa será configurado como será tratada a ficha financeira no sistema.  
   
**Parâmetros e Campos**  
Remove eventos zerados na liberação de competência  
Marque este parâmetro para que os eventos zerados que estão na Ficha Financeira e na Ficha Financeira por Centro de Custo sejam removidos no momento da liberação da competência.

Meses a manter na ficha financeira  
Informe a quantidade de meses que será armazenado na Ficha Financeira na Liberação da Competência.

**Observação**  
Em versão anteriores, o sistema armazenava somente 24 meses e realizava a transferência do restante para a Ficha Financeira complementar, mas se existisse a necessidade de realizar um cálculo de Férias em dobro observando as médias do período aquisitivo determinado, onde teria que buscar os eventos na Ficha Financeira Complementar e isto não era possível. Com esta flexibilidade de armazenamento será possível manter os meses desejados na Ficha Financeira.  
   
**Atenção**  
Alertamos que se o usuário utilizar a quantidade de meses maior que 36, poderá comprometer a performance do sistema.  
Período para gravar base de FGTS de afastados  
Informe o número do período para que seja gravada na Ficha Financeira, a base de FGTS de funcionários afastados por Acidente de Trabalho.

**Atenção**  
O sistema somente criará o período informado, para funcionários afastados por acidente de trabalho, após proceder a Liberação de Competência  
Processar grupo AAS na Ficha Financeira na liberação de competência

Manutenção da Ficha Financeira após período acima  
Selecione a opção para definir o que acontece com os meses da ficha financeira superior a quantidade de meses informado no campo 'Meses a manter na ficha financeira'.

* Remove da Ficha Financeira: Marcando esta opção assim que completar os meses, o sistema irá remover os meses da ficha financeira e não serão salvos na ficha financeira complementar os meses superiores a quantidade informada.
* Transfere da Ficha Financeira para Complementar: Marcando esta opção assim que completar os meses, o sistema irá armazenar os meses na Ficha Financeira complementar os meses superiores a quantidade informada.

**Observação**  
Este parâmetro somente é valido para usuários que efetuam o lançamento do grupos de eventos simultaneamente.

Visualização dos eventos com valores zerados no envelope   
Se você marcar este campo, todos os eventos com valores zerados irão ser visualizados no envelope. É importante lembrar que estes eventos não foram removidos da ficha Financeira do funcionário. Apenas não estão sendo exibidos na janela.  
**Observação**  
Esta opção também é valida para visualização de envelopes por centro de custo.

Visualizar o valor do salário-hora no envelope  
Marcando este parâmetro, o sistema irá habilitar na visão do envelope, o salário hora do funcionário.

Recalcular bases automaticamente no envelope  
O recálculo automático das bases tem a finalidade de eliminar divergência de valores de bases na folha analítica com a aba incidência do envelope de pagamento. Caso ocorra alteração no envelope de pagamento e o parâmetro "Recalcular bases automaticamente no envelope" esteja marcado, o sistema passa a calcular as bases automaticamente, da seguinte forma:  
Ao clicar em sim na mensagem: "Alguns valores do envelope foram alterados manualmente" o recalculo total é realizado e as bases são recalculadas.  
Ao clicar em não na mensagem: "Alguns valores do envelope foram alterados manualmente" é recalculado somente as bases. 

Recalcular automaticamente o envelope

Quando o parâmetro 'Recalcular automaticamente o envelope' estiver marcado, o usuário acessar o envelope de pagamento e fizer alguma alteração, ao clicar em salvar ou OK deverá recalcular o envelope sem exibir a mensagem abaixo:

Observação:

Quando o parâmetro 'Recalcular automaticamente o envelope' estiver marcado o parâmetro 'Recalcular bases automaticamente no envelope' será desabilitado.

---

<<Voltar para tela anterior **Folha Normal**
