---
content_hash: ebb58463d1aa8e72e2985855bfd5cff80c814007a83d5df123ec81f8fd87587b
fetched_at: '2026-06-29T00:05:51.973236+00:00'
page_id: '1056144007'
product: rm
source: tdn-rm
title: Dados do prestador de serviços (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144007
version: 2
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **prestador** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **1-1** | **Tag ráiz para as informações sobre o prestador.** |  |  |
| inscmun | prestador | E | 1-1 | Inscrição municipal do prestador. | GFILIAL.INSCMUN | Inscrição Municipal do prestador do serviço cadastrada na Filial do RM.  Para manter a máscara da inscrição municipal é necessário marcar a opção de "Não Remover Máscara IM Prestador" nos [dados fiscais do município.](https://tdn.totvs.com/pages/viewpage.action?pageId=652399054) |
| cpfcnpj | prestador | E | 1-1 | CPF/CNPJ do prestador. | GFILIAL.CGC |  |
| razao | prestador | E | 1-1 | Razão social do prestador. | GFILIAL.NOME |  |
| fantasia | prestador | E | 1-1 | Nome fantasia do prestador. | GFILIAL.NOMEFANTASIA |  |
| codmunibge | prestador | E | 0-1 | Código do município do prestador padrão IBGE |  | Código de Classificação definido para o município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| codmunsiafi | prestador | E | 0-1 | Codigo do município do prestador padrão SIAFI |  | Código de Classificação definido para o município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| cidade | prestador | E | 0-1 | Nome da cidade do prestador. | GMUNICIPIO.NOMEMUNICIPIO |  |
| uf | prestador | E | 1-1 | Unidade federativa do prestador. | GFILIAL.ESTADO |  |
| email | prestador | E | 0-1 | Endereço de e-mail do prestador. | GFILIAL.EMAIL |  |
| ddd | prestador | E | 0-1 | DDD do telefone do prestador. | GFILIAL.DDD |  |
| telefone | prestador | E | 0-1 | Telefone do prestador. | GFILIAL.TELEFONE |  |
| simpnac | prestador | E | 0-1 | Optante pelo regime simples nacional. Os conteúdos possíveis são:  •  1 – Sim;  •  2 – Não. | DFILIAL.OPTANTESIMPLES | Se DFILIAL.OPTANTESIMPLES > 0 Entao Sim Senao Não |
| incentcult | prestador | E | 0-1 | Incentivador cultural. Os conteúdos possíveis são:  •  1 – Sim;  •  2 – Não. | TMOVCOMPL.INCENTIVCULTURAL | Se TMOVCOMPL.INCENTIVCULTURAL Preenchido Entao Sim Senao Não |
| numproc | prestador | E | 0-1 | Número do processo judicial ou administrativo de  suspensão da exigibilidade | DPROCESSOJUDICIAL.NUMERO | Processo Judicial ou Administrativo Vinculado |
| logradouro | prestador | E | 1-1 | Descrição do logradouro do prestador. | GFILIAL.RUA |  |
| numend | prestador | E | 1-1 | Numero do endereço do prestador. | GFILIAL.NUMERO |  |
| bairro | prestador | E | 1-1 | Nome do bairro do prestador. | GFILIAL.BAIRRO |  |
| tplogradouro | prestador | E | 0-1 | Tipo de logradouro.  Os valores válidos são:  •  1 – Avenida;  •  2 – Rua;  •  3 – Rodovia;  •  4 – Ruela;  •  5 – Rio;  •  6 – Sítio;  •  7 – Sup Quadra;  •  8 – Travessa;  •  9 – Vale;  •  10 – Via;  •  11 – Viaduto;  •  12 – Viela;  •  13 – Vila  •  14 – Vargem. | DTIPORUA.DESCRICAO | Será verificado se DTIPORUA.DESCRICAO coincide com algum item da lista ao lado |
| cep | prestador | E | 1-1 | CEP do prestador. | GFILIAL.CEP |  |
| complemento | prestador | E | 0-1 | Complemento do endereço do prestador. | GFILIAL.COMPLEMENTO |  |
| caepf | prestador | E | 0-1 | Número do Cadastro de Atividade Econômica da Pessoa Física do prestador do Serviço. | GFILIAL.CADATIVECONOMICAPF | Será verificado se o número do cadastro sem a máscara possui mais de 14 caracteres, caso positivo, será enviado vazio mesmo que esteja preenchido. |
