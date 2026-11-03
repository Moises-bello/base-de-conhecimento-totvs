---
article_id: 360053561574
category: RH - Integração de Titulo
content_hash: 2cc9fc55193ecea4774417ec25b92160c09ef6152635dc73584d6685c197c2f1
fetched_at: '2026-06-28T22:43:36.358871+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de títulos com cadastro automático de fornecedor
  não cria o fornecedor corretamente
type: support-article
updated_at: '2025-07-23T20:09:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053561574-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-t%C3%ADtulos-com-cadastro-autom%C3%A1tico-de-fornecedor-n%C3%A3o-cria-o-fornecedor-corretamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33658102907415)**Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**Geração de títulos com cadastro automático de fornecedor não cria o fornecedor corretamente.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17.  
  
**Causas**1) Configuração incorreta;  
2) Ausência de amarração entre Participantes x Fornecedor;  
3) Não foram criados automaticamente os relacionamentos da tabela RD0 e RDZ, no momento do  cadastro de funcionário.   
  
**Solução**  
Para solucionar cada uma das ocorrências, realize os seguintes passos:

1. Confira a documentação, se a configuração foi realizada corretamente:  
[MP - GPE - Cadastro Automático de Fornecedores com as informações de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015466272-MP-GPE-Cadastro-Autom%C3%A1tico-de-Fornecedores-com-as-informa%C3%A7%C3%B5es-de-Funcion%C3%A1rios)  
2. Caso o fornecedor já esteja cadastrado, verifique as amarrações entre Participantes x Fornecedor:   
[MP - GPE - Geração de títulos não grava fornecedor já cadastrado no financeiro, gerando um novo fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054076053)  
  
3. Crie relacionamento entre o cadastro de funcionário x participantes.

-> Confira se os funcionários possuem CPF em seu cadastro, apenas os registros com CPF serão carregados na rotina de participantes;

-> Extraia/substitua o arquivo MSRELRDZ dentro da sua pasta System (anexo);

-> Certifique-se que o ambiente esta atualizado conforme portal, com Pacote Acumulado, Lib e Binário, e realize um backup das tabelas RD0 e RDZ.

-> Acesse o Modulo 53 em Atualizações -> Participantes -> Cadastros -> Outras ações -> Relacionar. Selecione Relacionar e deixe a rotina processar. Dependendo da quantidade de registros em sua SRA poderá demorar um pouco o processamento. Realize este processo de forma exclusiva, sem usuário utilizando qualquer rotina que possa envolver a tabela SRA (cadastro de funcionário).  
  
O sistema irá considerar todos os registros em sua SRA e relacionar nas tabelas RD0 e RDZ.

**Informações adicionais:**

Diferença entre relacionar e atualizar:

**Relacionar**  
Esta opção permite relacionar os dados do Cadastro de Funcionários (tabela SRA) com os dados do Cadastro de Pessoas/Participantes (tabela RD0). Este relacionamento é feito pelo número do CPF do Participante/Funcionário e atualiza a tabela (tabela RDZ) Pessoas x Entidades.  
  
Ao selecionar esta opção é apresentada a mensagem de confirmação Relacionar funcionários inativos?. Quando informar Sim, os funcionários demitidos são importados do Cadastro de Pessoas com o Status Ativo.  
  
**Atualizar**Esta opção permite apenas a atualização dos dados cadastrais do colaborador, por exemplo quando há uma alteração de *Status*, para Demitido.

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
