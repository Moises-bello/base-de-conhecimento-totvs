---
content_hash: eec6e0635b81630d1c82bca8dafe358cb2e82e9b8d6339af04856cac6a6c641a
fetched_at: '2026-06-29T00:09:47.215794+00:00'
page_id: '435104990'
product: rm
source: tdn-rm
title: Baixa por Demonstrativo Cronograma Desembolso
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+por+Demonstrativo+Cronograma+Desembolso
version: 11
---

**Baixa por Demonstrativo Cronograma Desembolso**

---

Após a Criação do contrato, medições da obra, podemos realizar o pagamento das parcelas do Plano de Financiamento. Neste processo, iremos executar a baixa de parcelas do Contrato.  
Iremos inserir o arquivo DCD - Demonstrativo de Cronograma Desembolso, que irá verificar em cada contrato as parcelas a serem baixadas pelo sistema, efetuando a baixa também no Financeiro.   
Este arquivo é gerado pela Caixa Econômica Federal.  
Cada linha do arquivo contém informações relacionadas a uma parcela de uma venda do Minha Casa Minha Vida.

* Localizar a Venda Para encontrar a venda que deve ser processada, o sistema lê o campo **NU\_CONTRATO OU IdContrato** da linha no arquivo e busca a venda que contenha este número de contrato na sua regra de venda no componente Financiamento CEF.
* Encontrando a Parcela Ao encontrar a venda, o sistema lê o campo **DT\_PARCELA** do arquivo, que corresponde a Data de Vencimento da parcela na venda e assim identifica de qual parcela se trata.

          O campo **NU\_PARCELA OU PAR** identifica o número da parcela que será baixada;

* Processamento do Arquivo Só serão processadas as linhas cujo campo **CO\_ESTADO\_PARCELA OU STATUS**estiver com o valor "LP" (Liberada Paga). Este campo indica que a parcela deve ser baixada.
* Conferindo Valores Uma vez localizada a parcela o sistema confere os valores que se encontram no arquivo com os valores dos componentes, que compõe a parcela, considerando uma margem de +/- R$ 0,03, como se segue:

**VR\_FGTS**: Este campo do arquivo, tem seu valor consistido com o componente "Fgts CEF"  
**VR\_RECURSO\_PROP\_MUTUARIO OU REC MUTUÁRIO**: Este campo do arquivo, tem seu valor consistido com o componente "Recurso Mutuário CEF"  
**VR\_SUBSIDIO OU DESCONTO**: Este campo do arquivo, tem seu valor consistido com o componente "Subsídio CEF"  
**VR\_FINANC\_MUTUARIO OU FIN MUTUÁRIO**: Este campo do arquivo tem seu valor consistido de acordo com a seguinte regra:

Importante

* Todos os campos citados em negrito deveram estar citados no arquivo .txt criado para o processamento da baixa por DCD, na primeira linha do arquivo. As demais linhas deverão conter os valores correspondentes a cada campo em uma única linha para cada contrato.
* Deverá ter o mesmo número de dados separados por ';', que a linha do cabeçalho, se não tiver o processamento não ocorrerá corretamente.
* Em casos de única parcela, onde será utilizada para ir efetuando as baixas de acordo com as liberações do banco, deve ser informado apenas na coluna '**REC MUTUÁRIO**' o valor disponibilizado para pagamento.
* Somente será efetuada a baixa da linha que contiver a coluna '**STATUS**' com o valor "**LP**"

Venda com parcela MCMV valor R$ 120000,00 e deseja executar um DCD para baixa parcial com valor de R$ 20000,00:

Deve ser criado o arquivo de acordo com o exemplo de Layout:  
      idContrato;DT PARCELA;PAR;STATUS;FGTS;REC MUTUARIO;DESCONTO;FIN MUTUARIO  
      21229000 ;01/06/2022  ;1    ;LP        ;0.00  ;20000.00           ;0.00            ;0.00

**Observação****:**  
Se for a primeira parcela e o contrato incluir terreno, então ele é consistido com o valor somado dos componentes "Terreno CEF" e "Financiamento CEF".  
Se não for a primeira parcela ou o contrato não incluir terreno, então ele é consistido apenas com o valor do componente "Financiamento CEF".  
Se algum destes valores não for consistente, o processo não baixa a parcela e gera um Log do erro encontrado.

Se o empreendimento do contrato MCMV não possuir medição com avanço associado e existir apenas uma parcela com o valor total do financiamento gerado para o contrato de venda, ao realizar uma baixa via arquivo DCD do respectivo contrato será realizada uma **baixa parcial** na parcela única no valor total encontrado no DCD para cada competência encontrada no arquivo DCD. A baixa parcial porém irá seguir a regra de baixa definida do financeiro, respeitando os tipos de baixa por prioridade e proporcional, conforme estiver definido no financeiro. Sendo assim os valores de Terreno, FGTS, Financiamento, Subsidio e Recurso Mutuário serão baixados parcialmente respeitando a configuração de tipo de baixa por prioridade ou proporcional.

Importante

Uma vez cadastrado medição para o empreendimento e possuir lançamentos baixados através da medição não será possível realizar a baixa parcial, visto que o empreendimento não pode ter nenhuma medição cadastrada.

Vídeo demonstrativo:

250
