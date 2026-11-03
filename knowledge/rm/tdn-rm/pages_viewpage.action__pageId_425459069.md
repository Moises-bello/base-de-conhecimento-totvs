---
content_hash: c5e5f2a601573f334b4d0de52182643651148eaf0a945e9d63171d24eb9332f9
fetched_at: '2026-06-29T00:09:33.862592+00:00'
page_id: '425459069'
product: rm
source: tdn-rm
title: Identificar faltas em aulas práticas, teóricas, estagio e laboratório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459069
version: 3
---

O plano de aula foi alterado para a inclusão de um tipo de aula que pode ser: teórica, prática, estágio ou laboratório. Assim é possível detalhar a frequência do aluno por este tipo de aula, caso esteja devidamente parametrizado.

As funcionalidades: Geração do plano de aula, Cadastro de Plano de aula, Criação de estrutura de oferta integração com o Scientia e geração de plano de aula sequencial formam alteradas com a inclusão deste campo tipo de aula.

No portal e no Educa Mobile, além de visualizar o tipo de aula o professor tem a opção de alterar mediante permissão na segurança do perfil de acesso do Totvs Educacional.

Assim acesse: Totvs Educacional | Outras permissões | RM Portal | Acadêmico | Professor | Diário de Classe| Plano de Aula | Permitir alteração do Tipo da Aula.

O Aluno consegue visualizar o tipo de aula através do plano de aula existente no portal e no educa mobile.

Foi desenvolvida a função de fórmula "TotalFaltaPorTipoAula", para retornar com o total de faltas do aluno de acordo com o seu tipo de aula. Passando com parâmetro T – Teórica; P- Prática; E – Estágio; L – Laboratório.

No quadro de aviso é possível exibir ou não o detalhamento da frequência do aluno, caso queira visualizar é necessário marcar o parâmetro que está em secretaria | Geral 3/5 | Exibir aviso de frequência por tipo da aula.

A central de notificações, permite enviar um e-mail informando que a frequência do aluno está próxima do limite ou exercido, foi alterada para realizar o envio caso o percentual de faltas de algum tipo de aula atinja o limite de falta parametrizada em Secretária | Geral 3/5 | Limite de Faltas.  
    
 **OBS.: Implementação disponibilizada apenas para o contexto do Ensino Superior.**

Veja Também

---

[Documento Técnico - Identificar faltas em aulas práticas, teóricas, estágio e laboratório](http://tdn.totvs.com/display/LRM/DT_Identificar_faltas_aulas_praticas_teoricas_estagio_e_laboratorio)
