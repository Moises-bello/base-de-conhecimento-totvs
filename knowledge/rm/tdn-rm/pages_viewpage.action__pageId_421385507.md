---
content_hash: 041c9d00801c451fedd88bb77b7b44ac8a34d915557472ece522f1597a2ba095
fetched_at: '2026-06-29T00:09:16.296721+00:00'
page_id: '421385507'
product: rm
source: tdn-rm
title: Cálculo Produção da Equipe Mecânica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385507
version: 3
---

---

Siga os passos abaixo para efetuar o cálculo de produção da equipe mecânica:

1. Abra a visão de composições;
2. Edite a composição por produção para o qual deseja efetuar o cálculo de produção da equipe mecânica;
3. Abra a pasta 'Prod. de Equipe Mecânica';
4. Clique em 'Inserir Equipe'. São associados os insumos que não são percentuais e que pertencem ao grupo DNIT A - Equipamentos;
5. No campo 'Chefe da Equipe', selecione o equipamento que será o chefe da equipe;
6. Preencha as variáveis intervenientes;
7. Informe a fórmula que será utilizada no cálculo da produção horária. A fórmula pode conter parênteses, números e os operadores +, - \* e /.

**Exemplo:**

(B\*G\*H\*I\*60)/S

8. Clique no botão 'Calcula produção horária' para calcular a produção horária de cada equipamento que possui uma fórmula associada, seguindo a mesma. O resultado da aplicação da fórmula será exibido no campo 'Produção horária';

9. Clique no botão 'Simulação' para efetuar uma simulação baseada na produção horária calculada. Serão propostos valores para os campos de num. de unidades (quantidade), utilização produtiva (coeficiente produtivo) e utilização improdutiva (coeficiente improdutivo). Cálculos efetuados: Núm. de unidades = produção da equipe / produção horária. O resultado desse valor é sempre arredondado para o inteiro superior, ou seja, se o resultado for 3,1, ele será arredondado para 4. Utilização produtiva = produção da equipe / (número de unidades do equipamento que está sendo calculado \* produção horária do equipamento que se está calculando a utilização). A utilização produtiva do equipamento chefe é produção da equipe / (núm. de unidades \* produção horária). Se a utilização produtiva for maior que 1, o valor da mesma será 2 menos o valor da utilização apurado. Utilização improdutiva = 1 – utilização produtiva. O campo 'Produção Equipe' exibe o conteúdo do campo 'Produção por hora' existente na pasta Identificação da composição. Este campo pode ser modificado para efetuar simulações;

10. Clique no botão 'Atualiza composição' para transferir os valores dos campos produção horária, num. de unidades, utilização produtiva e utilização improdutiva para a pasta Identificação da composição.

11. Imprima uma planilha com os dados do cálculo da produção das equipes mecânicas.

**Observação:**

Os campos de variáveis intervenientes (de A a V) obedecem ao número de casas decimais dos coeficientes especiais (pasta Exibição, F6).

O campo 'Produção da equipe' exibe a produção da última simulação efetuada.

Clique no botão "Unidades" caso deseje efetuar o cadastramento de uma unidade para cada variável interveniente da composição editada.

A unidade será a mesma para todos os equipamentos da composição.
