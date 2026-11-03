---
article_id: 32267518489623
category: eSocial - Tabelas/Não Periódicos
content_hash: f1908e81c31ad9d367b1f47d361ef36e9b8156f37864957b7b2f0b4d1b05d459
fetched_at: '2026-06-28T22:47:10.234983+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Ajuste no evento S-2206 para preservação dos dados
  do Aprendiz em alterações de Categoria
type: support-article
updated_at: '2026-06-05T17:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32267518489623-RH-RM-FOP-eSocial-Ajuste-no-evento-S-2206-para-preserva%C3%A7%C3%A3o-dos-dados-do-Aprendiz-em-altera%C3%A7%C3%B5es-de-Categoria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32267518463255) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
Ao alterar a categoria eSocial de “103 - Aprendiz” para “101 - Empregado”, o sistema desabilita automaticamente a aba “Dados do Aprendiz” e limpa todos os campos preenchidos. Dessa forma, ao gerar o evento S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária, as informações sobre o aprendiz não são incluídas no envio.   
   
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da versão: 12.1.2406 e superiores  
  
**Solução**  
Houve uma implementação no produto para garantir a correta geração das informações do aprendiz, mesmo em casos de alteração da categoria eSocial.

Para isso, foram realizados ajustes no menu **Administração de Pessoal > Funcionários > Aba Registro**, de modo que, ao alterar a categoria de "103 - Aprendiz" para "101 - Empregado", a aba **"Dados do Aprendiz"** permaneça habilitada, preservando as informações previamente registradas.  
  
Para solucionar, siga os passos abaixo:   
1. É necessário, no menu **Administração de Pessoal | Funcionários | Históricos | Histórico da Categoria eSocial**, verificar se existe um registro com o código da Categoria eSocial igual a **103 (Aprendiz)**;

![image-2025-4-25_9-36-48.png](https://tdn.totvs.com/download/attachments/937703589/image-2025-4-25_9-36-48.png?version=1&modificationDate=1745585653550&api=v2)

**Exemplo:**  
Funcionário admitido como **aprendiz** em **01/10/2023**com a Categoria eSocial preenchida com  "103 - Aprendiz**".**  
Em **01/08/2024**, o funcionário teve a alteração de categoria para **"101 - Empregado"**.  
Com a nova tratativa, mesmo após a mudança de categoria, a aba **"Dados do Aprendiz"** permanece habilitada e com as informações preenchidas, pois existe um histórico de categoria "**103 - Aprendiz"** registrado.

![image-2025-4-25_14-54-2.png](https://tdn.totvs.com/download/attachments/937703589/image-2025-4-25_14-54-2.png?version=1&modificationDate=1745603642610&api=v2)

Assim, ao gerar o evento **S-2206**, as informações relacionadas ao aprendiz continuam sendo corretamente enviadas no grupo <aprend>.

Para o exemplo mencionado acima, no mês de **07/2024** foi gerado o evento **S-2206**, com data de alteração em **01/07/2024**, ainda com o funcionário na categoria eScocial "103-Aprendiz"  
Observe que o grupo <aprend> foi gerado corretamente, conforme demonstrado no print abaixo;

![image-2025-4-25_15-47-7.png](https://tdn.totvs.com/download/attachments/937703589/image-2025-4-25_15-47-7.png?version=1&modificationDate=1745606827707&api=v2)

Já no mês de 04/2025, foi gerado outro evento **S-2206**, com data de alteração em **25/04/2025**, agora com o funcionário na categoria eScocial "101-Empregado".

Observe que, nesse caso, o grupo <aprend> **não foi gerado corretamente**, conforme demonstrado abaixo;

![image-2025-4-25_17-19-16.png](https://tdn.totvs.com/download/attachments/937703589/image-2025-4-25_17-19-16.png?version=1&modificationDate=1745612356833&api=v2)

Saiba mais:   
[Mapeamento S-2206](https://tdn.totvs.com/display/LRM/Evento+S-2206)
