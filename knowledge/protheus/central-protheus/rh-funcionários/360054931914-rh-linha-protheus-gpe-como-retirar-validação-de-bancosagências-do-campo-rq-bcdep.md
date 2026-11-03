---
article_id: 360054931914
category: RH - Funcionários
content_hash: 5e5c0d9d57b3256445c580c78b2b474621c3aa53e02e883a792d459bafaff6e5
fetched_at: '2026-06-28T22:43:27.694064+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como retirar validação de Bancos/Agências do campo
  RQ_BCDEPBE do Cadastro de Beneficiários
type: support-article
updated_at: '2025-06-11T20:15:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054931914-RH-Linha-Protheus-GPE-Como-retirar-valida%C3%A7%C3%A3o-de-Bancos-Ag%C3%AAncias-do-campo-RQ-BCDEPBE-do-Cadastro-de-Benefici%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25198145450775) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como retirar validação de Bancos/Agências do campo RQ\_BCDEPBE do cadastro de beneficiários  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o Módulo **Configurador (SIGACFG)**  
2. Acesse **Base de Dados > Dicionários >  Base de dados**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190267671)  
  
  
3. Clique no sinal seta para baixo para expandir as opções e depois clique em **Dicionários de Dados  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460219994391)**4. Clique na **lupa,** pesquise pela tabela **SRQ** e depois clique em **buscar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190276503)  
  
5. Clique em **Editar** e abra a visualização dos **Campos**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220000919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190284695)

6. Selecione o campo **RQ\_BCDEPBE**e clique em **Alterar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220007319)  
  
  
7. Na aba **Opções,**deixe em branco o conteúdo do campo **Cons. Padrão;**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220009751)

8. Após salvar, clique em **sair** das configurações do Dicionário de Dados  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220012311)  
  
  
9. Clique em **Atualizar Base de Dados**, no ícone de disquete para gravar as alterações. Para que esta ação seja executada corretamente, nenhum usuário pode estar logado no Sistema (Modo exclusivo).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220014615)

10. **Avance** as telas para que o sistema efetive o ajuste no campo e ao final, clique em**Finalizar.****![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220017559)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190301975)**

11. Acesse a tabela SX3 filtrada pelo campo RQ\_BCDEPBE no banco de dados, eretire o conteúdo do campo X3\_VALID.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190303511)**  
  
Na visualização via Configurador ficará da seguinte forma **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460190307607)**Após alterações, no cadastro do beneficiário a rotina permite o usuário preencher o campo sem necessidade de existir o banco/agência gravado na tabela SA6:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460220033175)**  
**Atenção:**

* Os campos: **banco, agência e conta** são desconsiderados no grupo de campos do Configurador (SIGACFG), pois podem ou não estar vinculados ao cadastro de bancos (SA6). O vínculo obrigatório ao cadastro de bancos, implicaria em uma série de validações do módulo Financeiro (SIGAFIN), que poderia não atender a todos os clientes.
* A alteração do campo é caracterizada como **customização,** portanto a sua alteração e validação é de **responsabilidade do cliente.**

 

**Saiba Mais**

[RH - Linha Protheus - GPE - Qual o programa para o cadastro de Bancos e Agências Bancárias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015715632-RH-Linha-Protheus-GPE-Qual-o-programa-para-o-cadastro-de-Bancos-e-Ag%C3%AAncias-Banc%C3%A1rias?source=search)  
[RH - Linha Protheus - GPE - Geração e Impressão de Cheques](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012457072-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-e-Impress%C3%A3o-de-Cheques?source=search)  
[RH - Linha Protheus - GPE - Onde alterar os dados cadastrais do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016407931-RH-Linha-Protheus-GPE-Onde-alterar-os-dados-cadastrais-do-funcion%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar banco/agência com dígito verificador X](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052965754-RH-Linha-Protheus-GPE-Como-cadastrar-banco-ag%C3%AAncia-com-d%C3%ADgito-verificador-X?source=search)
