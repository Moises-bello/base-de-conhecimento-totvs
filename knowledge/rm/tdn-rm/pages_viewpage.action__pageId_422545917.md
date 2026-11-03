---
content_hash: 4fdaedddc39a89f5919f0cdab2eb3be3e7c7aa859a6e9ad3f0978f1b44be806a
fetched_at: '2026-06-29T00:09:21.812761+00:00'
page_id: '422545917'
product: rm
source: tdn-rm
title: Sub Apuração (Detalhamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545917
version: 9
---

Foi criado um Processo no Período de Apuração para o tributo ICMS que execute os cálculos descritos abaixo. Juntamente a este processo, foi criado o Anexo do Período de Apuração, Prodepe - Sub-Apuração ICMS, para armazenar os Detalhes da Sub-Apuração, contendo as seguintes informações:

**1. Código da Sub-Apuração**  
Código da Sub-Apuração a que se refere o detalhamento.

**2. Indicador do enquadramento do benefício**  
Indicador do enquadramento do benefício informado no Cadastro de Benefícios Fiscais.

**3. Saídas não incentivadas**  
Somatório do Valor Contábil de todos os Lançamentos de Saída dos produtos associados à Sub-Apuração, cujo CFOP associado ao lançamento é "Fiscal" e NÃO está parametrizado como operação incentivada no Cadastro da Sub-Apuração.

**4. Saídas incentivadas**  
Este campo só será preenchido para os enquadramentos "Industrial e Central de Distribuição".  
Somatório do Valor Contábil dos Lançamentos de Saída dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração.

**5. Saídas incentivadas - Faixa 1**  
Este campo só será preenchido para o enquadramento "Importador".  
Somatório do Valor Contábil dos Lançamentos de Saída em operações internas (CFOPs 5.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração. Devem ser totalizados aqui apenas as movimentações dos Produtos da Sub-Apuração que possuem a alíquota interna até 7% (sete por cento) - Anexo "Dados Fiscais por UF" do Cadastro do Produto.

**6. Saídas incentivadas - Faixa 2**  
Este campo só será preenchido para o enquadramento "Importador".  
Somatório do Valor Contábil dos Lançamentos de Saída em operações internas (CFOPs 5.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração. Devem ser totalizados aqui apenas as movimentações dos Produtos da Sub-Apuração que possuem a alíquota interna maior que 7% (sete por cento) e menor igual à 12% (doze por cento) - Anexo "Dados Fiscais por UF" do Cadastro do Produto.

**7. Saídas incentivadas - Faixa 3**  
Este campo só será preenchido para o enquadramento "Importador".  
Somatório do Valor Contábil dos Lançamentos de Saída em operações internas (CFOPs 5.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração. Devem ser totalizados aqui apenas as movimentações dos Produtos da Sub-Apuração que possuem a alíquota interna maior que 12% (doze por cento) e menor igual à 17% (dezessete por cento) informada no Anexo "Dados Fiscais por UF" do Cadastro do Produto.

**8. Saídas incentivadas - Faixa 4**  
Este campo só será preenchido para o enquadramento "Importador".  
Somatório do Valor Contábil dos Lançamentos de Saída em operações internas (CFOPs 5.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração. Devem ser totalizados aqui apenas as movimentações dos Produtos da Sub-Apuração que possuem a alíquota interna maior que 17% (dezessete por cento) informada no Anexo "Dados Fiscais por UF" do Cadastro do Produto.

**9. Saídas incentivadas para fora do Nordeste**  
Este campo só será preenchido para o enquadramento "Industrial".  
Dos Lançamentos selecionados para geração das "Saídas incentivadas" (item 4), subtotalizar aqueles cuja UF do Cliente/Fornecedor é diferente de: MA, PI, CE, RN, PB, AL, SE, BA e PE.

**10. Saídas incentivadas para fora do Estado**  
Este campo só será preenchido para o enquadramento "Importador". Somatório do Valor Contábil dos Lançamentos de Saída em operações interestaduais (CFOPs 6.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração.

**11. ICMS das saídas incentivadas p/fora do Estado**  
Este campo só será preenchido para o enquadramento "Importador".  
Para os lançamentos selecionados nas "Saídas incentivadas para fora do Estado" (item 10), deve ser informado, neste campo, o valor do ICMS destacado no Lançamento Fiscal.

**12. Importações com ICMS diferido**  
Este campo só será preenchido para o enquadramento "Importador".  
Somatório do Valor Contábil dos Lançamentos de Entrada em operações de importação (CFOPs 3.xxx) dos produtos associados à Sub-Apuração e cujo CFOP, associado ao lançamento, esteja mapeado como sendo operação incentivada, também no Cadastro da Sub-Apuração.

**13. ICMS diferido nas importações**  
Este campo só será preenchido para o enquadramento "Importador".  
Para os lançamentos selecionados nas "Importações com ICMS diferido" (item 12), deve ser informado, neste campo, o valor do ICMS que foi diferido na operação, Valor do ICMS desonerado do Item do Lançamento Fiscal.

**14. Entradas não incentivadas**  
Este campo só será preenchido para o enquadramento "Centrais de Distribuição".  
Somatório do Valor Contábil de todos os Lançamentos de Entrada dos produtos associados à Sub-Apuração, cujo CFOP associado ao lançamento é "Fiscal" e NÃO está parametrizado como operação incentivada no Cadastro da Sub-Apuração.

**15. Entradas incentivadas**  
Este campo só será preenchido para o enquadramento "Centrais de Distribuição".  
Somatório do Valor Contábil de todos os Lançamentos de Entrada dos produtos associados à Sub-Apuração, cujo CFOP associado ao lançamento é "Fiscal" e está parametrizado como operação incentivada no Cadastro da Sub-Apuração.

**16. Saldo credor do período anterior**  
Este campo deve ser preenchido com o campo "Saldo devedor/credor do período" (item 33) do Período de Apuração imediatamente anterior da Sub-Apuração, se credor.

**17. Total de crédito do ICMS das entradas**  
Totalizar o valor do ICMS que gerou crédito nas entradas dos produtos incentivados, associados à Sub-Apuração.

**18. Total de outros créditos**  
Totalizar os Lançamentos de Outros Débitos/Crédito do Tipo "Crédito", associados à Sub-Apuração.

**19. Total de estornos de débito**  
Totalizar os Lançamentos de Outros Débitos/Crédito do Tipo "Estorno de Débito", associados à Sub-Apuração.

**20. Total de débito do ICMS das saídas**  
Totalizar o valor do ICMS que gerou débito nas saídas dos produtos incentivados, associados à Sub-Apuração.

**21. Total de outros débitos**  
Totalizar os Lançamentos de Outros Débitos/Crédito do Tipo "Débito", associados à Sub-Apuração.

**22. Total de estornos de crédito**  
Totalizar os Lançamentos de Outros Débitos/Crédito do Tipo "Estorno de Crédito", associados à Sub-Apuração.

**23. Saldo devedor ANTES das deduções do Prodepe**  
Fórmula: ("Saldo credor do período anterior" + "Total de crédito do ICMS das entradas" + "Total de outros créditos" + "Total de estornos de débito") - ("Total de débito do ICMS das saídas" + "Total de outros débitos" + "Total de estornos de crédito")  
Observação: Os campos 16 a 23 têm a mesma sistemática da apuração atual do ICMS. O diferencial está no fato de que essa apuração será por Sub-Apuração vigente.

**24. Valor do crédito presumido nas operações para fora do NE**  
Este campo só será preenchido para o enquadramento "Industrial".  
Valor resultante da aplicação do percentual do crédito presumido para estas operações informado na Sub-Apuração, sobre o valor das "Saídas incentivadas para fora do Nordeste" (item 9).  
Se o Saldo devedor do ICMS relativo à faixa incentivada (Total de débito do ICMS das saídas - Total de crédito do ICMS das entradas) for menor ou igual 0, este campo deve ser igual a 0.

**25. Valor do crédito presumido nas saídas interestaduais**  
Este campo só será preenchido para o enquadramento "Importador".  
Valor resultante da aplicação do percentual do crédito presumido nas saídas Interestaduais informado na Sub-Apuração, sobre o valor do "ICMS das saídas incentivadas p/fora do Estado" (item 11).

**26. Crédito Presumido nas saídas internas (Faixa 1)**  
Este campo só será preenchido para o enquadramento "Importador".  
Valor resultante da aplicação do Percentual de crédito presumido para as saídas internas - Faixa 1 informado na Sub-Apuração, sobre o valor das Importações com ICMS diferido (item 13).

**27. Crédito Presumido nas saídas internas (Faixa 2)**  
Este campo só será preenchido para o enquadramento "Importador".  
Valor resultante da aplicação do Percentual de crédito presumido para as saídas internas - Faixa 2 informado na Sub-Apuração, sobre o valor das Importações com ICMS diferido (item 13).

**28. Crédito Presumido nas saídas internas (Faixa 3)**  
Este campo só será preenchido para o enquadramento "Importador".  
Valor resultante da aplicação do Percentual de crédito presumido para as saídas internas - Faixa 3 informado na Sub-Apuração, sobre o valor das Importações com ICMS diferido (item 13).

**29. Crédito Presumido nas saídas internas (Faixa 4)**  
Este campo só será preenchido para o enquadramento "Importador".  
Valor resultante da aplicação do Percentual de crédito presumido para as saídas internas - Faixa 4 informado na Sub-Apuração, sobre o valor das Importações com ICMS diferido (item 13).

**30. Valor do crédito presumido**  
Este campo só será preenchido para o enquadramento "Industrial".  
Valor resultante da aplicação do percentual do crédito presumido informado na Sub-Apuração, sobre o saldo devedor relativo à faixa incentivada após o crédito presumido nas saídas p/fora do NE.

**31. Crédito presumido nas entradas incentivadas**  
Este campo só será preenchido para o enquadramento "Central de Distribuição".  
Valor resultante da aplicação do Percentual de incentivo para as entradas informado na Sub-Apuração, sobre o valor das Entradas incentivadas.

**32. Crédito presumido nas saídas incentivadas**  
Este campo só será preenchido para o enquadramento "Central de Distribuição".  
Valor resultante da aplicação do Percentual de incentivo para as saídas informado na Sub-Apuração, sobre o valor das Saídas incentivadas.

**33. Saldo devedor/credor do período**  
\*Industrial:\* Fórmula: "Saldo devedor ANTES das deduções do Prodepe" - "Valor do crédito presumido nas operações para fora do NE" - "Valor do crédito presumido".  
Se o \[Percentual de crédito presumido\] for maior ou igual a 70%, o \[Saldo devedor/credor do período\] não pode ser inferior a 15% do \[Saldo devedor ANTES das deduções do Prodepe\]. Se isso acontecer, o valor do crédito presumido nas saídas para fora do Nordeste deve ser reduzido.  
Se o \[Percentual de crédito presumido\] for menor que 70%, o \[Saldo devedor/credor do período\] não pode ser inferior a 30% do \[Saldo devedor ANTES das deduções do Prodepe\]. Se isso acontecer, o valor do crédito presumido nas saídas para fora do Nordeste deve ser reduzido.  
\***Importador**:\* Fórmula: "Saldo devedor ANTES das deduções do Prodepe" - "Valor do crédito presumido nas saídas interestaduais" - "Crédito Presumido nas saídas internas (Faixa 1)" - "Crédito Presumido nas saídas internas (Faixa 2)" - "Crédito Presumido nas saídas internas (Faixa 3)" - "Crédito Presumido nas saídas internas (Faixa 4)"  
\***Central de Distribuição**:\* Fórmula: "Saldo devedor ANTES das deduções do Prodepe" - "Crédito presumido nas entradas incentivadas" - "Crédito presumido nas saídas incentivadas".  
No cálculo do Valor Contábil dos campos acima devem ser \*desconsiderados\* os CFOPs 1.933, 2.933, 3.933, 5.933, 6.933 e 7.933 por se tratarem de operações de serviços registrados em documento autorizado pelo Estado. Deve-se desconsiderar também, o valor da substituição tributária que porventura esteja somado ao Valor Contábil.

Para cada Sub-Apuração é preciso conhecer:

* O total das saídas dos produtos associados à Sub-Apuração;
* Desse total, qual o valor das saídas cuja operação não está na faixa de incentivo (o CFOP NÃO está associado à Sub-Apuração);
* E o total das saídas que estão na faixa de incentivo (cujo CFOP foi associado à Sub-Apuração).
* A soma dos dois últimos itens tem que ser igual ao primeiro.
* Saldo Devedor do ICMS próprio no Período de Apuração já é calculado considerando os lançamentos de ajustes do período.

No Período de Apuração para armazenar o Saldo credor/devedor do ICMS antes das deduções do Prodepe. Ao encerrar o Período de Apuração, o sistema alimenta os campos: "Saldo Credor/Devedor" e "Saldo Credor/Devedor antes Prodepe".   
Ao processar as Sub-Apurações, o sistema insere um lançamento de ajuste do Tipo "Crédito" para o tributo ICMS, para cada Sub-Apuração processada, com o valor total do crédito presumido apurado (itens 24 à 32 acima). O código da Sub-Apuração deve ser gravado no lançamento de ajuste no novo campo, conforme descrito no item 3.1.3 deste documento.  
No Período de Apuração, o sistema deve atualizar o campo "Saldo Credor/Devedor" para que reflita o real valor do imposto a ser pago.
