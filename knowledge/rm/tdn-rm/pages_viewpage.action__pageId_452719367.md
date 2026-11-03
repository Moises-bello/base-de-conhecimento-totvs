---
content_hash: 36526630810586f7e326f44af1b7ac60fe7034be1606b7387ea8fdef859d2726
fetched_at: '2026-06-29T00:10:07.132355+00:00'
page_id: '452719367'
product: rm
source: tdn-rm
title: Guia de INSS por Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719367
version: 6
---

falseATENÇÃO!

A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

A Guia de INSS por dissídio (GPS 650) é uma guia específica para recolhimento das verbas relacionadas a diferenças por dissídio.

A GPS 650 é gerada utilizando o mesmo assistente de execução de processo da guia de folha e décimo terceiro. A diferença está em duas flags criadas na tela de geração, a saber:  
·          Dissídio  
·          Incluir Reclamatória Trabalhista – CC202  
É importante destacar que a Guia de INSS por dissídio gera o layout impresso e lançamento financeiro com os mesmos cálculos do SEFIP 650 e regras da Guia de INSS emitida pelo validador do SEFIP.  
   
**Parâmetros**  
Com o parâmetro "Dissídio" marcado, este passo irá se comportar da seguinte maneira:  
   
·          O novo parâmetro "Incluir Reclamatória Trabalhista – CC 202" será habilitado. Quando marcado, o valor do evento de código de cálculo "202 Reclamatória Trabalhista" será somado à Base de INSS, quando o evento for provento ou base;  
·          Os campos "Tipo de Guia", "Opções", "Utilizar percentual redutor (Lei 12.546/2011)" e "Tipo de Percentual Redutor" serão desabilitados e os checkboxes serão demarcados;  
·          Os campos "% Autônomos" e "% Cooperativa" serão desabilitados e seus valores preenchido com zero;  
·          O Campo "Tipo de Guia" assumirá a opção "Folha";  
·          Os demais campos estarão habilitados para edição.  
   
**Opções para geração**  
Quando a opção "Dissídio" estiver marcada no passo anterior, não será habilitada a opção de GPS Eletrônica.  
**Integrações**  
Quando estiver sendo gerada a Guia de INSS por dissídio, este passo do assistente não será habilitado.  
**Parâmetros específicos por coligada**  
Na aba "Geral", os campos "Outros Sistemas", "Opções", "Utilizar Percentual redutor (Lei 12.546/2011)",  "Tipo de Percentual Redutor", "% Autônomos" e "% Cooperativa" serão desabilitados. Os demais campos estarão habilitados para edição.  
Quando marcado o campo "Dissídio" no passo "Parâmetros" dos parâmetros gerais, a aba "Retificação" ficará oculta e as demais abas ("Lançamento Financeiro" e "Eventos não considerados") continuarão com o mesmo funcionamento.  
O lançamento financeiro continuará a ser dos mesmos tipos utilizados na Guia de INSS normal.  
**Lógica de Cálculo**  
Todos os eventos considerados nos cálculos de valores da Guia de INSS por dissídio são obtidos a partir da Ficha Financeira (Envelope) do funcionário.  
Os funcionários pertencentes às categorias descritas abaixo não serão processados na Guia de INSS por dissídio. Tais categorias também não são processadas no SEFIP 650, a saber:  
·         11 - Diretor não-empregado sem FGTS (empresário)  
·         17 - Cooperado da cooperativa de trabalho  
·         18 - Transp. cooperado prestando serv. Contratantes de coop. de trab.  
·         24 - Cont. Ind. cooperado que presta serviços a ent. Beneficente  
·         25 - Cont. Ind. transportador cooperado que presta serv. ent. benef.  
·         Código de Categoria não preenchido  
**Base de INSS**  
A base de INSS será composta da seguinte maneira:  
Funcionário:  
·         Soma dos eventos com código de cálculos 69 ou 111, se forem do tipo base;  
·         Soma dos eventos de código de cálculo 202, se forem dos tipos base ou provento e se o parâmetro "Incluir Reclamatória Trabalhista - CC202" estiver marcado;  
·         Subtração dos eventos de código de cálculo 99, se houver incidência de INSS e FGTS no evento e a soma dos eventos com códigos de cálculo 69, 111 e 202 for maior ou igual à soma dos eventos com código de cálculo 99 (essa subtração é necessária pois, nessas condições, o valor do 99 foi incluído no 69);  
·         Soma dos eventos de código de cálculo 109, se forem dos tipos base ou provento;  
·         Soma dos eventos de código de cálculo 98, se forem dos tipos base ou provento e houver incidência de FGTS13 e INSS13 no evento.  
   
OBS: É importante ressaltar que em certas situações pode haver determinação judicial quanto ao valor que deve ser pago ao funcionário. Quando ocorre esse tipo de particularidade, poderá ser lançado o valor determinado pela justiça em um evento com código de cálculo 202 que seja provento ou base de cálculo. Nesse caso, basta marcar a flag 'Incluir Reclamatória Trabalhista – CC 202' para que o evento seja considerado para a base de cálculo, juntamente com os outros eventos.  
   
Autônomo:  
·         Soma dos eventos de código de cálculo 46, se o autônomo for das categorias 5, 13, 14, 15 ou 16 e o evento for do tipo base ou provento;  
·         Subtração dos eventos de código de cálculo 46, se o autônomo for das categorias 5, 13, 14, 15 ou 16 e o evento for do tipo desconto;  
·         Como estes cálculos foram baseados no SEFIP 650, a regra acima é a composição dos campos 16 - "Remuneração sem 13º"e 22 - "Base de Cálculo 13º Salário Previdência Social" do SEFIP.  
   
**Base de INSS para Aposentadoria Especial 15, 20 e 25 anos**  
·         Será a mesma base calculada para Base de INSS  
·         Sob a base acima será aplicado o percentual conforme informado no cadastro de seção, a saber:  
o    Para ocorrências 2 e 6 do SEFIP, será aplicado o % de INSS 15 Anos  
o    Para ocorrências 3 e 7 do SEFIP, será aplicado o % de INSS 20 Anos  
o    Para ocorrências 4 e 8 do SEFIP, será aplicado o % de INSS 25 Anos

**Segurados**  
·         Será a mesma base calculada para Base de INSS  
·         Sobre a base acima será aplicado o percentual adequado, conforme informado no cadastro de seção, a saber:   
o    Para ocorrências 2 e 6 do SEFIP, será aplicado o % de INSS 15 Anos  
o    Para ocorrências 3 e 7 do SEFIP, será aplicado o % de INSS 20 Anos  
o    Para ocorrências 4 e 8 do SEFIP, será aplicado o % de INSS 25 Anos

**Acidente de Trabalho e Terceiro**  
A GPS emitida pelo validador do SEFIP 650 não calcula o valor de Acidente de trabalho e de Terceiros para as categorias abaixo:  
·         5 - Diretor não-empregado com FGTS (empresário)  
·         11 - Diretor não-empregado sem FGTS (empresário)  
·         13 - Trab. Autônomo ou equiparado c/ contrib. sobre remuneração  
·         14 - Trab. Autônomo ou equiparado c/ contrib. sobre salário-base  
·         15 - Transportador autônomo c/ contrib. sobre remuneração  
·         16 - Transportador autônomo c/ contrib. sobre salário-base  
O mesmo comportamento da GPS emitida pelo validador do SEFIP foi aplicado à GPS 650 do sistema. Para as demais categorias, o sistema segue o cálculo padrão da GPS.

**Percentuais**  
Os percentuais serão os mesmos já informados na GPS e registrados no cadastro de seção, a saber:  
·         Parâmetro "% Empresa" da Guia de INSS;  
·         Percentuais de Juros e Multas da Guia de INSS;  
·         Campo "Percentual acidente de trabalho" do cadastro de seção, aba "Dados p/ INSS";  
·         Campo "Percentual de terceiros" do cadastro de seção, aba "Dados p/ INSS";  
·         Alíquota do FAP com vigência da competência de pagamento registrado no anexo "FAP Estabelecimento Empresarial" do cadastro de seção;  
·         Os percentuais de INSS 15, 20 e 25 anos também na aba "Dados p/ INSS".

**Seções e Valores da Seção**  
Ao gerar a GPS por dissídio, os campos e botões que não são pertinentes ficarão desabilitados, a saber:  
·         Botão "Atualizar Saldo de Comp. e Ret."  
·         Campos "Autônomos", "Autônomos não cad.", "INSS Aut. (M.P. 83)", "Compensação/reembolso", 'Sal. Matern. não deduz.", "Deduções", "Valor cooperativas", "Valores anteriores", "Retenção".

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Guia de INSS Dissidio](http://tdn.totvs.com/pages/viewpage.action?pageId=351020560)
