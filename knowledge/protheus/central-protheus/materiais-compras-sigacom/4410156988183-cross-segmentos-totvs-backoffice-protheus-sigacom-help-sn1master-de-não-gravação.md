---
article_id: 4410156988183
category: Materiais - Compras (SIGACOM)
content_hash: a1c4941891eafe46fa06367080cb36e6765ed7f604e566f9dad12819f8d416af
fetched_at: '2026-06-28T22:41:18.786091+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help "SN1MASTER" de
  Não gravação da tabela SF9 ao incluir Documento de Entrada com o Ativo Fixo
type: support-article
updated_at: '2022-10-26T13:58:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410156988183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-SN1MASTER-de-N%C3%A3o-grava%C3%A7%C3%A3o-da-tabela-SF9-ao-incluir-Documento-de-Entrada-com-o-Ativo-Fixo
---

**Dúvida**Ao incluir um documento de entrada onde o TES esteja configurado para integrar com o ativo e com o CIAP, sistema apresenta o help :

SN1MASTER  
N1\_CODCIAP  
REGNOIS  
Não existe registro relacionado a chave informada no alias SF9, ordenação 1.  
1) Informe um código que exista no cadastro.  
2) Efetue o cadastro no programa de manutenção do respectivo cadastro.  
3) Escolha um registro válido.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Para o correto funcionamento do sistema no tocante ao controle de numeração da tabela SF9 e atualização da tabela SN1, temos 2(duas) possíveis soluções para serem avaliadas, como forma mais confiável de alteração de criação de código iniciado por caracteres, nestes casos envolvendo SF9 e SN1

*Opção 1 :*  
  
Alterar o parâmetro **MV\_FSNCIAP**( Tipo de numeração do código de sequencia do CIAP: 1=Código gravado no momento do lançamento do bem, 2=Código no formato 9999/99.) para 2, assim, a numeração será composta pelos 4 primeiros caracteres + barra + 2 caracteres referentes ao ano corrente, porem o controle de numeração não fica mais a cargo do sistema, pois a sequência de código vai depender do ultimo código lançado na tabela SF9 :  
Ex: Se estivermos no ano de 2021  
De    "IM7869"  
Para  "IM79/21"  
Para  "IM8A/21"  
Para  "IM8B/21"

*Opção 2 :*  
Quando parâmetro **MV\_FSNCIAP igual a "1**"(Neste caso com o controle de numeração feito pelo sistema conforme configuração feita no SIGACFG), alterar o parâmetro **MV\_SOMAOLD**( Se .T. habilita comportamento antigo na execução da função Soma1()) para .T. , pois assim o comportamento da criação de códigos sequenciais seria:

MV\_SOMAOLD = .T. (Idêntico ao comportamento das sequencias via controle de numeração feita pelo SIGACFG )  
EX:   
De    "IM7469"  
Para  "IM7470"  
Para  "IM7471" 

MV\_SOMAOLD = .F.  
EX:   
De    "IM7469"  
Para  "IM747A"  
Para  "IM747B"

Logo, quando o parâmetro MV\_SOMAOLD = .T. o comportamento da função Soma1() passa a ser idêntico ao da função GETSXENUM(Que faz o controle das numerações sequenciais das tabelas automaticamente via SIGACFG) , porem, é importante frisar que a função Soma1() é utilizada em diversos módulos como forma de criar números sequenciais, como exemplo, sequência de itens de notas fiscais, de títulos à pagar e à receber, dentre outros.

***Caso seja detectada alguma inconsistência na tabela SF9, será necessário acionar a equipe de suporte ao módulo Livros Fiscais.***

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
