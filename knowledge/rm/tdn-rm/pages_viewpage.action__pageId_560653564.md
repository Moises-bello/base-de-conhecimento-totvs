---
content_hash: f3aeb379dee90ab08af8012eaaeb3201f4e2f7c63baa82ebb905f06d021ea7ca
fetched_at: '2026-06-29T00:10:47.694019+00:00'
page_id: '560653564'
product: rm
source: tdn-rm
title: Aproveitamento de campos complementares do candidato para o registro de aluno
  e de responsável financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653564
version: 14
---

# Sumário

---

Sumário

# Regras

---

Para que essa cópia aconteça algumas regras devem ser seguidas:

1. O campo complementar **deve existir em ambos os cadastros**;
2. O **nome da coluna** deve ser o mesmo em ambos os cadastros;
3. O **tipo do campo** complementar dever ser o mesmo em ambos os cadastros;
4. Caso o campo seja real ou alfanumérico. **eles devem possuir a mesma escala ou o mesmo tamanho** em ambos os cadastros;
5. Se o valor no campo de origem for nulo, o valor no campo de destino não será apagado.

# Cadastros

---

Serão considerados os campos complementares dos seguintes cadastros:

* Caso o processo seletivo **utilize** o novo portal de inscrições, o sistema irá consultar os campos complementares da inscrição do candidato e, de acordo com a regra, copiá-los para os campos complementares do cadastro de aluno.

Caminhos dos campos complementares:

***Educacional | Processo Seletivo | Campos complementares | Campos complementares | Inscrição e matrícula de candidato***

***Educacional | Educacional | Configurações | Configuração | Campos complementares | Aluno***

* Caso o processo seletivo **não utilize** o novo portal de inscrição, o sistema irá consultar os campos complementares do cadastro de pessoa, no módulo de Gestão de Pessoas, para os campos complementares do cadastro de aluno.

Caminhos dos campos complementares:

***RH | Gestão de Pessoas | Acompanhamento | Pessoas | Campos Complementares | Pessoa***

***Educacional | Educacional | Configurações | Configuração | Campos complementares | Aluno***

Caso o parâmetro para cadastro do responsável financeiro do aluno esteja marcado para a definição do próprio aluno como responsável financeiro, o sistema irá tentar copiar os campos complementares, também, para o cadastro de cliente/fornecedor do responsável do aluno.

Esse parâmetro pode ser encontrado no processo de matrícula de candidatos aprovados, no Educacional, e, também, na parametrização para o Venda on-line, no cadastro de Área de interesse ofertada, no Processo Seletivo.

Caminhos dos campos complementares:

***Educacional | Educacional | Configurações | Configuração | Campos complementares | Aluno***

***BackOffice | Gestão Financeira | Cadastros | Específicos | Campos Complementares | Clientes/Fornecedores***

# Comportamento

---

* **Parametro "*Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro*" marcado:**

Caso o parâmetro esteja marcado, ao realizar a matrícula de um candidato aprovado em um processo seletivo ou através de venda on-line, o sistema irá consultar todos os parâmetros cadastrados para o candidato e irá realizar a cópia das informações para os mesmos campos no cadastro do aluno.

* **Parametro "*Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro*" desmarcado:**

Os dados dos campos complementares disponíveis na matrícula do portal do processo seletivo ([para mais informações sobre a parametrição de campos complementares no processo seletivo clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=444608352)) serão aproveitados para o aluno e o responsável financeiro, seguindo as regras estabelecidas nesta documentação.

Os campos complementares serão aproveitados no momento de efetivação da matrícula do candidato, seguindo as regras dispostas nesta documentação.

# Parametrização

---

Através do parâmetro "*Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro*" é possível copiar todas as informações complementares de um candidato para o seu cadastro de aluno no Educacional, independente da disponibilidade dos campos complementares na inscrição ou matrícula.

Esse parâmetro pode ser encontrado em:

***Educacional | Educacional | Configurações | Configuração | Parâmetros***

***15.03 - Matrícula | Movimento 4/4 | Processo seletivo RM | "Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro"***
