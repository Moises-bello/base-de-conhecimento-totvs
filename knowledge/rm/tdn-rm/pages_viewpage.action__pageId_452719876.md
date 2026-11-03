---
content_hash: 6f6895479d318348c7b0691d2aa3be4b08cb1868e0da2c4603f0b432594b21f1
fetched_at: '2026-06-29T00:10:10.562134+00:00'
page_id: '452719876'
product: rm
source: tdn-rm
title: Endereço - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719876
version: 2
---

Pasta destinada ao cadastramento do endereço completo da seção, incluindo endereço de pagamento (para líquidos bancários).  
    
 O tipo de logradouro deve ser informado para ser considerado no arquivo de e-Social.   
    
 Passos para tipo de logradouro ser informado no e-Social no arquivo S-1020 (Tab. Lotações):

1. Cadastrar no módulo de BackOffice / Gestão Fiscal / Mais / Endereço / Classificação de Tipo de Rua
2. Cadastrar o código do Tipo de Rua conforme tabela e-Social no módulo de BackOffice / Gestão Fiscal / Mais / Endereço / Tipo de Rua / anexo Codificação de Tipo de Rua
3. Cadastrar no parametrizador do módulo RH / Folha de Pagamento, o Conceito de Classificação para Tipo de Rua (De/Para) conforme item 1.

O Telefone deve ser cadastrado somente com 7 ou 8 dígitos para gerar SEFIP corretamente, ou seja, o arquivo busca estes números para informação.   
    
 **Exemplo:**  
 3333-3333 ou 333-3333  
    
 O Endereço de Pagamento (P/ Líquidos Bancários) é relativo à geração de layout de alguns líquidos bancários para o gerador de relatórios.  
    
 O E-mail será utilizado para informação no arquivo de RAIS, ou seja, deve ser preenchido principalmente nas seções centralizadoras do arquivo de RAIS.  
    
 Marcando o campo Endereço alterado será informado no SEFIP, registro do tipo 10 – Informações da Empresa (seções) que houve alteração de endereço da seção.  
    
 Para cadastro de município foi criado uma **lupa** para que caso não saiba o código do município do sistema, na lupa você já consegue verificar juntamente com a cidade o código de município dela.  
 Caso seja diferente do código do IBGE você possui a permissão para alterar o campo 'código do município' colocando da forma correta.  
    
 **Exemplo**  
 Londrina. No sistema você não sabe qual é o código, já no site do IBGE é 4113700.  
 Agora quando você procura pela Lupa o estado Londrina, juntamente é acompanhado o código da cidade no sistema.  
    
 **Observação**   
 Coloque o Estado primeiramente antes de buscar na 'lupa' o município
